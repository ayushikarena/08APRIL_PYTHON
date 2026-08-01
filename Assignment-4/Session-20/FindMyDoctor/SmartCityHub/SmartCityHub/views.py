from django.shortcuts import render
from restaurant.models import Restaurant

def home(request):
    popular_restaurants = Restaurant.objects.order_by('-rating')[:3]
    return render(request, 'home.html', {'popular_restaurants': popular_restaurants})
