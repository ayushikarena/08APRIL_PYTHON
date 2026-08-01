from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# Add Product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


# Product List
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


# Edit Product
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})


# Delete Product
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'delete_product.html', {'product': product})