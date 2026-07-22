# app/urls.py
# Maps URL paths to views for the application.

from django.urls import path
from . import views

urlpatterns = [
    # Route for the homepage
    path('', views.home, name='home'),
    
    # Route for finding a restaurant location and map (Task 2)
    path('restaurant-map/', views.show_restaurant_location, name='restaurant_map'),
    
    # Route for searching nearby Flipkart Pickup Points (Task 4)
    path('search-distance/', views.search_by_distance, name='search_distance'),
]
