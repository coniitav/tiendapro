from django.urls import path
from .views import index, cart, detail, add_to_cart
from .auth_views import sign_up, sign_up_create, sign_in, sign_out

urlpatterns = [
    path("", index, name="index"),
    path("cart", cart, name="cart"),
    path("product/<code>", detail, name="detail"),
    path("add_to_cart/<code>", add_to_cart, name="add_to_cart"),
    path("sign_up", sign_up, name="sign_up"),
    path("sign_up/create", sign_up_create, name="sign_up_create"),
    path("sign_in", sign_in, name="sign_in"),
    path("sign_out", sign_out, name="sign_out"),
]