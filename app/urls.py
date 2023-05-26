from django.urls import path
from django.contrib import admin
from rest_framework import routers
from crm.viewsets import Customerlist
from django.conf.urls import include

router = routers.DefaultRouter()
router.register("customers", Customerlist, basename="customers")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api.auth/", include("rest_framework.urls")),
    path("admin", admin.site.urls)
]