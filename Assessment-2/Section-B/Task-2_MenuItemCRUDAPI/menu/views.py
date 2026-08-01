from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemListCreateAPIView(APIView):
    """
    APIView for getting all menu items and creating a new menu item.
    """
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuItemDetailAPIView(APIView):
    """
    APIView for retrieving, updating, and deleting a single menu item.
    """
    def get_object(self, id):
        try:
            return MenuItem.objects.get(id=id)
        except MenuItem.DoesNotExist:
            return None

    def get(self, request, id):
        menu_item = self.get_object(id)
        if not menu_item:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        menu_item = self.get_object(id)
        if not menu_item:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = MenuItemSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        menu_item = self.get_object(id)
        if not menu_item:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)
            
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
