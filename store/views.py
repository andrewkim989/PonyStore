from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import View

from .models import Product
from .forms import Productform

class Home (View):
    def get(self, request):
        return render(request, "home.html", {"product": Productform() })

class Products (View):
    def get(self, request):
        return render(request, "products.html", {"products": Product.objects.all()})
    
    def post(self, request):
        e = []
        form = Productform(request.POST)
        errors = form.errors.items()

        if not form.is_valid():
            for key, value in errors:
                e.append(value)
            return HttpResponse(e, content_type = "application/json")
        else:
            Product.objects.create(brand = request.POST["brand"], name = request.POST["name"], 
            price = request.POST["price"], description = request.POST["description"])
            return redirect("/products")

class SingleProduct (View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        data = {"brand": product.brand, "name": product.name, "price": product.price,
        "description": product.description}
        context = {
            "prod": Productform (initial = data),
            "product": product
        }
        return render(request, "info.html", context)

class EditProduct(View):
    def post(self, request, id):
        e = []
        form = Productform(request.POST)
        errors = form.errors.items()

        if not form.is_valid():
            for key, value in errors:
                e.append(value)
            return HttpResponse(e, content_type = "application/json")
        else:
            p = Product.objects.get(id = id)
            p.brand = request.POST["brand"]
            p.name = request.POST["name"]
            p.price = request.POST["price"]
            p.description = request.POST["description"]
            p.save()
            return redirect("/products")
    
    def get(self, request, id):
        Product.objects.get(id = id).delete()
        return redirect("/products")

def sortByBrand(request):
    return render(request, "products.html", {"products": Product.objects.all().order_by("brand")})

def sortByName(request):
    return render(request, "products.html", {"products": Product.objects.all().order_by("name")})

def sortByPrice(request):
    return render(request, "products.html", {"products": Product.objects.all().order_by("price")})

def sortByCreated(request):
    return render(request, "products.html", {"products": Product.objects.all().order_by("created_at")})

def sortByUpdated(request):
    return render(request, "products.html", {"products": Product.objects.all().order_by("updated_at")})