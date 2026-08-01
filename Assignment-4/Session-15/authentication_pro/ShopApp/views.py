from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from .models import *

@login_required
def my_orders(request):
    return render(request,'my_orders.html')


@permission_required('ShopApp.add_product',raise_exception=True)
def post_product(request):
    return render(request,'post_product.html')

#=========================Task-3===========================

@permission_required('ShopApp.add_review', raise_exception=True)   # Use your app name here
def add_review(request):
    if request.method == "POST":
        movie = request.POST.get("movie")
        review = request.POST.get("review")

        Review.objects.create(
            movie=movie,
            review=review
        )

        return redirect("view_review")   # or redirect("add_review")

    return render(request, "add_review.html")


@permission_required('ShopApp.view_review',raise_exception=True)
def view_review(request):
    return render(request,'view_review.html')

#=========================Task-4===========================


@login_required
def dashboard(request):

    if request.user.groups.filter(name='Seller').exists():
        return render(request,'seller_dashboard.html')

    elif request.user.groups.filter(name='Buyer').exists():
        return render(request,'buyer_dashboard.html')

    else:
        return render(request,'home.html')