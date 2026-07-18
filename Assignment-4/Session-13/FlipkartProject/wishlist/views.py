from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def home(request):
    products = Product.objects.all()

    return render(request, "home.html", {
        "products": products
    })


def delete_product(request, id):

    if request.method == "DELETE":

        try:
            product = Product.objects.get(id=id)
            product.delete()

            return JsonResponse({
                "success": True
            })

        except Product.DoesNotExist:

            return JsonResponse({
                "success": False,
                "message": "Product not found"
            })

    return JsonResponse({
        "success": False,
        "message": "Invalid request"
    })