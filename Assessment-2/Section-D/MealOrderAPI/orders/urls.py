from django.urls import path
from .views import PlaceOrderAPIView, ListOrdersAPIView

urlpatterns = [
    # POST endpoint for placing orders
    path('place/', PlaceOrderAPIView.as_view(), name='place-order'),
    
    # GET endpoint for viewing all orders
    path('list/', ListOrdersAPIView.as_view(), name='list-orders'),
]
