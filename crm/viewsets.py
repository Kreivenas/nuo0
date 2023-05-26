from rest_framework import viewsets, authentication, permissions
from .serializers import CustomerSerializer
from .models import Customer

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