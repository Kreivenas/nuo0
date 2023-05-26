from rest_framework import viewsets, authentication, permissions
from .serializers import CustomerSerializer, EventSerialize
from .models import Customer, Event

class Customerlist(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [
        permissions.DjangoModelPermissions,
    ]

    def get_queryset(self):
        return Customer.objects.all()

class EventList(viewsets.ModelViewSet):
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [
        permissions.DjangoModelPermissions,
    ]

    serializer_class = EventSerialize

    def get_queryset(self):
        return Event.objects.all()