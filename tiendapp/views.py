from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "tiendapp/index.html")

def cart(request):
    context = {
        "items": [None, None, None, None]
    }
    return render(request, "tiendapp/cart.html", context)

def detail(request):
    context = {

    }
    return render(request, "tiendapp/product_detail.html", context)