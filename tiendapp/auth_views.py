from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tiendapp.models import Customer

def sign_up(request):
    return render(request, "tiendapp/sign_up.html")

def sign_up_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print(">>>>>>>>>", data)

        nuevo_user = User.objects.filter(username = data["email"]).first()
        if nuevo_user is not None:
            return redirect("/sign_up")
        
        if nuevo_user is None:
            nuevo_user = User()
            nuevo_user.first_name = data["nombres"]
            nuevo_user.last_name = data["apellidos"]
            nuevo_user.username = data["email"]
            nuevo_user.is_active = True
            nuevo_user.save()

            nuevo_user.set_password("123456")
            nuevo_user.save()
        
        nuevo_customer = Customer.objects.filter(user = nuevo_user).first()
        if nuevo_customer is None:
            nuevo_customer = Customer()
            nuevo_customer.user = nuevo_user # Enlace
            nuevo_customer.billing_address = data["direccion"]
            nuevo_customer.shipping_address = "Av. Libertad 3434. Concepcion."
            nuevo_customer.phone = data["telefono"]
            nuevo_customer.save()
    
    return redirect("/sign_in")

def sign_in(request):
    from django.contrib.auth import authenticate, login
    if request.method == "POST":
        data = request.POST.copy()
        username = data["username"]
        password = data["password"]

        usuario_valido = authenticate(request, username = username, password = password)

        if usuario_valido is not None:
            login(request, usuario_valido)
            return redirect("/")
        else:
            # incluir mensaje de error
            pass

    return render(request, "tiendapp/sign_in.html")