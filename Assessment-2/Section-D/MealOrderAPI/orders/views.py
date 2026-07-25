from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .models import Order

class PlaceOrderAPIView(APIView):
    """
    API endpoint that allows food delivery orders to be placed.
    """
    def post(self, request, *args, **kwargs):
        # 1. Pass the incoming request data to the serializer
        serializer = OrderSerializer(data=request.data)
        
        # 2. Check if the provided data is valid based on model and serializer validations
        if serializer.is_valid():
            # 3. If validation succeeds, save the order to the database
            serializer.save()
            
            # 4. Return the saved order details (including auto-generated id) with HTTP 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 5. If validation fails (e.g., negative quantity), return errors with HTTP 400 Bad Request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListOrdersAPIView(APIView):
    """
    API endpoint to view all orders.
    """
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
