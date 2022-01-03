from django.shortcuts import render
from .models import Product


def index_page(request):
    print(f"User {request.user}")
    products = Product.objects.all()

    data = {"movie": "a good data", "products": products}
    return render(request, "index.html", data)


def contact_page(request):
    return render(request, "contact.html")


def product_page(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, "product.html", context)
