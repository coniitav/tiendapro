from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    productos = Product.objects.all()
    context = {
        "items": productos
    }
    return render(request, "tiendapp/index.html", context)

def cart(request):
    context = {
        "items": [None, None, None, None]
    }
    return render(request, "tiendapp/cart.html", context)

def detail(request, code):
    producto = Product.objects.get(sku = code)
    context = {
        "producto": producto
    }
    return render(request, "tiendapp/product_detail.html", context)