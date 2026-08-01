from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    # ── Custom named-action URLs ──────────────────────────────────────────
    path('orders/retrieve/<int:pk>/',       OrderViewSet.as_view({'get':    'retrieve'}),       name='order-retrieve'),
    path('orders/create/',                  OrderViewSet.as_view({'post':   'create'}),          name='order-create'),
    path('orders/update/<int:pk>/',         OrderViewSet.as_view({'put':    'update'}),          name='order-update'),
    path('orders/partial-update/<int:pk>/', OrderViewSet.as_view({'patch':  'partial_update'}),  name='order-partial-update'),
    path('orders/delete/<int:pk>/',         OrderViewSet.as_view({'delete': 'destroy'}),         name='order-delete'),

    # ── Default router URLs (list, detail, filter, paginate) ──────────────
    path('', include(router.urls)),
]
