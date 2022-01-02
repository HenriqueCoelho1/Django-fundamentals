from django.contrib import admin

from .models import Product, Costumer


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class CostumerAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email")


admin.site.register(Product, ProductAdmin)
admin.site.register(Costumer, CostumerAdmin)
