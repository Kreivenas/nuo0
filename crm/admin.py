from django.contrib import admin
from .models import Customer, Category, Event

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Event)