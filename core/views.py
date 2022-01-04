from django.shortcuts import render, get_object_or_404
from .models import Product

from django.http import HttpResponse
from django.template import loader


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


def error404(request, ex):
    template = loader.get_template("404.html")
    return HttpResponse(
        content=template.render(), content_type="text/html; charset=utf8", status=404
    )


def error500(request):
    template = loader.get_template("500.html")
    return HttpResponse(
        content=template.render(), content_type="text/html; charset=utf8", status=500
    )
