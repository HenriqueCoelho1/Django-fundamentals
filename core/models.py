from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.name} with {self.stock}"


class Costumer(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} with {self.surname}"
