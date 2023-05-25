from django.db import models

COUNTRES = (
    ("LT", "Lithuania"),
    ("UK", "United Kingdom"),
    ("PL", "Poland"),
)

class Category(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)


class Customer(models.Model):
    name = models.CharField(max_length=1024)
    adress = models.CharField(max_length=1024)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=2, choices=COUNTRES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
