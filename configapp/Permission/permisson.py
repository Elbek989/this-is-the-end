from django.core.cache import cache
from rest_framework.permissions import BasePermission

class IsEmailVerified(BasePermission):
    def has_permission(self, request, view):
        email = request.data.get('email')
        if not email:
            return False
        return cache.get(f"{email}_verified") == True
