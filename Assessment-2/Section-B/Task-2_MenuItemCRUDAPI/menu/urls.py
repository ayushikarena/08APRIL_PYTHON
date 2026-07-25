from django.urls import path
from .views import MenuItemListCreateAPIView, MenuItemDetailAPIView

urlpatterns = [
    path('api/menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list'),
    path('api/menu-items/<int:id>/', MenuItemDetailAPIView.as_view(), name='menu-item-detail'),
]
