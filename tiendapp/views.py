from django.shortcuts import render, redirect
from .models import Product, ProductCategory

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
    
    categorias_relacionadas = ProductCategory.objects.filter(product = producto)
    categorias_relacionadas_id = [rel.category.id for rel in categorias_relacionadas]

    productos_sugeridos = ProductCategory.objects.filter(category__in = categorias_relacionadas_id).exclude(product = producto)
    
    productos_sugeridos_id = [ss.product.id for ss in productos_sugeridos]

    extras = Product.objects.filter(id__in = productos_sugeridos_id)

    context = {
        "producto": producto,
        "extras": extras
    }
    return render(request, "tiendapp/product_detail.html", context)

def add_to_cart(request, code):
    return redirect("/cart")