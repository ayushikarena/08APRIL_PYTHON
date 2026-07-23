from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, UserProfileView, CityViewSet, RestaurantViewSet, 
    MenuItemViewSet, CartView, CartItemView, OrderViewSet
)

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    # Auth endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profile
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    # Cart
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/items/', CartItemView.as_view(), name='cart-item-add'),
    path('cart/items/<int:pk>/', CartItemView.as_view(), name='cart-item-detail'),
    
    # Viewsets
    path('', include(router.urls)),
]
