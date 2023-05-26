from django.urls import path
from django.contrib import admin
from rest_framework import routers
from crm.viewsets import Customerlist, EventList
from django.conf.urls import include

router = routers.DefaultRouter()
router.register("customers", Customerlist, basename="customers")
router.register("events", EventList, basename="events")


urlpatterns = [
    path("api/", include(router.urls)),
    path("api.auth/", include("rest_framework.urls")),
    path("admin", admin.site.urls)
]
