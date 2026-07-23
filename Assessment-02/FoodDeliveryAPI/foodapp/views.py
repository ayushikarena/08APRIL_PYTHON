from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import City, Restaurant, MenuItem, Cart, CartItem, Order, OrderItem
from .serializers import (
    UserRegistrationSerializer, UserSerializer, CitySerializer,
    RestaurantSerializer, MenuItemSerializer, CartSerializer,
    CartItemSerializer, OrderSerializer
)
from decimal import Decimal

# Explanation of Statelessness with JWT Authentication:
# In a traditional Django application, authentication state is maintained using sessions.
# The server stores session data and sends a session ID cookie to the client.
# This requires the server to keep track of logged-in users, making it stateful.
# 
# JWT (JSON Web Token) authentication makes the API stateless.
# The server does not store any session data. When a user logs in, the server
# verifies the credentials and signs a JWT (containing user info and expiration time).
# The client stores this token (e.g., in localStorage or secure storage on mobile)
# and sends it in the Authorization header (Bearer <token>) with every request.
# The server validates the token's signature on each request.
# This is preferred for mobile and web frontends because it scales easily (no session storage needed)
# and works seamlessly across different domains and client types.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        city_id = self.request.query_params.get('city')
        cuisine = self.request.query_params.get('cuisine')
        
        if city_id:
            queryset = queryset.filter(city_id=city_id)
        if cuisine:
            queryset = queryset.filter(cuisine__icontains=cuisine)
            
        return queryset

    @action(detail=True, methods=['get'])
    def menu(self, request, pk=None):
        restaurant = self.get_object()
        menu_items = MenuItem.objects.filter(restaurant=restaurant, availability=True)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CartView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartSerializer

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class CartItemView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartItemSerializer

    def post(self, request):
        """Add item to cart or update quantity if it already exists."""
        cart, _ = Cart.objects.get_or_create(user=request.user)
        menu_item_id = request.data.get('menu_item')
        quantity = int(request.data.get('quantity', 1))

        if quantity <= 0:
            return Response({"error": "Quantity must be greater than zero"}, status=status.HTTP_400_BAD_REQUEST)

        menu_item = get_object_or_404(MenuItem, id=menu_item_id)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, 
            menu_item=menu_item,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = self.serializer_class(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    def patch(self, request, pk):
        """Update cart item quantity"""
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, id=pk, cart=cart)
        
        quantity = int(request.data.get('quantity', 1))
        if quantity <= 0:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        cart_item.quantity = quantity
        cart_item.save()
        return Response(self.serializer_class(cart_item).data)

    def delete(self, request, pk):
        """Remove item from cart"""
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, id=pk, cart=cart)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

    def create(self, request, *args, **kwargs):
        """Place an order from the user's cart"""
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = cart.items.all()
        
        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Assuming all items in the cart are from the same restaurant for simplicity
        # Or we group by restaurant. Let's enforce single restaurant per order.
        restaurant = cart_items.first().menu_item.restaurant
        for item in cart_items:
            if item.menu_item.restaurant != restaurant:
                return Response(
                    {"error": "All items in an order must be from the same restaurant. Please clear cart or order separately."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        total_amount = sum(Decimal(str(item.menu_item.price)) * item.quantity for item in cart_items)
        
        order = Order.objects.create(
            user=request.user,
            restaurant=restaurant,
            total_amount=total_amount,
            status='PENDING'
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                menu_item=item.menu_item,
                quantity=item.quantity,
                price=item.menu_item.price
            )

        # Clear the cart
        cart.items.all().delete()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
