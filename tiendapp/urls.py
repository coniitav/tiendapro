from django.urls import path
from .views import index, cart, detail

urlpatterns = [
    path("", index, name="index"),
    path("cart", cart, name="cart"),
    path("product/<code>", detail, name="detail"),
]