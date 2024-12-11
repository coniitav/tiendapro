from django.shortcuts import render
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
    categorias = [c.category_id for c in ProductCategory.objects.filter(product = producto)]
    productos_categorias = ProductCategory.objects.filter(category__in = categorias)
    extras = []
    for pc in productos_categorias:
        extras.append(pc.product)

    context = {
        "producto": producto,
        "extras": extras
    }
    return render(request, "tiendapp/product_detail.html", context)