from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PickupLocation

@login_required
def book_cab(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lng = request.POST.get('longitude')
        address = request.POST.get('address')

        if lat and lng and address:
            PickupLocation.objects.create(
                user=request.user,
                latitude=lat,
                longitude=lng,
                address=address
            )
            messages.success(request, 'Pickup location saved successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please select a valid location.')
            
    return render(request, 'map.html')
