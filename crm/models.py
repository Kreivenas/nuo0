from django.db import models
from django.conf import settings



COUNTRES = (
    ("LT", "Lithuania"),
    ("UK", "United Kingdom"),
    ("PL", "Poland"),
)

class Category(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Category={}".format(self.name)


class Customer(models.Model):
    name = models.CharField(max_length=1024)
    adress = models.CharField(max_length=1024)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=2, choices=COUNTRES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Customer name={self.name}", f"country={self.country}"

# class Event(models.Model):
#     comment = models.TextField()
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
#     crated = models.DateField(auto_created=True)
#     def __str__(self):
#         return "Evan By: {}", "customer: {}", "Time: {}".format(self.user, self.customer, self.crated)

class Event(models.Model):
    comment = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Event By: {}, customer: {}, Time: {}".format(self.user, self.customer, self.created)


class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
