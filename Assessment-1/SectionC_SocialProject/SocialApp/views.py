from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import ProfileForm
import csv
from django.http import HttpResponse


def profile_list(request):
    profiles = Profile.objects.all()

    return render(request, 'list.html', {
        'profiles': profiles
    })


def profile_create(request):

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')

    else:
        form = ProfileForm()

    return render(request, 'create.html', {
        'form': form
    })


def profile_edit(request, id):

    profile = get_object_or_404(Profile, id=id)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('list')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'create.html', {
        'form': form
    })


def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    writer = csv.writer(response)

    writer.writerow(['Name', 'Email', 'Age', 'City'])

    profiles = Profile.objects.all()

    for profile in profiles:
        writer.writerow([
            profile.name,
            profile.email,
            profile.age,
            profile.city
        ])

    return response
