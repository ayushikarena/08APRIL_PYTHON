from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def welcome(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'login.html', {'error': 'Invalid Username or Password'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')