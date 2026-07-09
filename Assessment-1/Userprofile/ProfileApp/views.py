from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def index(request):

    if request.method == "POST":
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = UserProfileForm()

    profiles = UserProfile.objects.all()

    context = {
        'form': form,
        'profiles': profiles
    }

    return render(request, 'index.html', context)

# Create your views here.
