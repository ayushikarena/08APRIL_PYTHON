from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

@login_required
def view_profile(request):
    return render(request, 'profile.html', {'profile': request.user.profile})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name', profile.full_name)
        profile.mobile = request.POST.get('mobile', profile.mobile)
        profile.address = request.POST.get('address', profile.address)
        profile.city = request.POST.get('city', profile.city)
        profile.state = request.POST.get('state', profile.state)
        profile.pincode = request.POST.get('pincode', profile.pincode)
        
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            
        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('view_profile')
        
    return render(request, 'edit_profile.html', {'profile': profile})
