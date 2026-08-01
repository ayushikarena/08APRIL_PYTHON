from django.urls import path
from .views import CategoryListView, MenuItemListCreateView, MenuItemDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('menu-items/', MenuItemListCreateView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:id>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
]
