from django.urls import path
from .views import index, cart, detail, add_to_cart

urlpatterns = [
    path("", index, name="index"),
    path("cart", cart, name="cart"),
    path("product/<code>", detail, name="detail"),
    path("add_to_cart/<code>", add_to_cart, name="add_to_cart"),
]