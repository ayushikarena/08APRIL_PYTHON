from django.urls import path
from .views import *

urlpatterns = [

    path("playlists/", PlaylistList.as_view()),

    path("orders/", OrderList.as_view()),

    path("cart/", CartList.as_view()),

    path("tickets/", TicketList.as_view()),

]