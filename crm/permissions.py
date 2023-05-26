from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user. is_superuser:
            return True
        if request.user == object.user:
            return True
        else:
            return False





