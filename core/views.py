from django.shortcuts import render, get_object_or_404
from .models import Product


def index_page(request):
    print(f"User {request.user}")
    products = Product.objects.all()

    data = {"movie": "a good data", "products": products}
    return render(request, "index.html", data)


def contact_page(request):
    return render(request, "contact.html")


def product_page(request, id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    context = {"product": product}
    return render(request, "product.html", context)
