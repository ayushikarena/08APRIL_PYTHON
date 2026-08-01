from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, MenuItem, Order
from .serializers import CategorySerializer, MenuItemSerializer, OrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer)

    def get(self, request, *args, **kwargs):
        # Allow GET requests so the browser can render the HTML form
        return Response({'message': 'Please use the HTML form below to POST your username and password.'})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by('id')
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def perform_create(self, serializer):
        # Automatically assign the request.user as the customer
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        return Order.objects.all().order_by('-created_at')
