from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer

class CategoryListView(ListAPIView):
    """
    API endpoint that allows categories to be viewed.
    Returns HTTP 200 OK with a JSON array of all Category records.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemListCreateView(APIView):
    """
    API endpoints for handling MenuItem lists and creation.
    """
    def get(self, request):
        """List all menu items."""
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new menu item."""
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuItemDetailView(APIView):
    """
    API endpoints for retrieving, updating, and deleting a single MenuItem.
    """
    def get_object(self, id):
        """Helper to get MenuItem instance or raise 404."""
        try:
            return MenuItem.objects.get(id=id)
        except MenuItem.DoesNotExist:
            raise Http404

    def get(self, request, id):
        """Retrieve a menu item by ID."""
        try:
            menu_item = self.get_object(id)
            serializer = MenuItemSerializer(menu_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        """Update a menu item."""
        try:
            menu_item = self.get_object(id)
            serializer = MenuItemSerializer(menu_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        """Delete a menu item."""
        try:
            menu_item = self.get_object(id)
            menu_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)
