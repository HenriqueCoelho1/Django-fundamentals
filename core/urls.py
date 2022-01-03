from django.urls import path

from .views import index_page, contact_page, product_page

urlpatterns = [
    path("", index_page, name="index"),
    path("contact/", contact_page, name="contact"),
    path("product/<int:id>", product_page, name="product"),
]
