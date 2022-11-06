from .models import Driver_job
from rest_framework.permissions import BasePermission , SAFE_METHODS

class DriverPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(

            request.user.is_authenticated and request.user.is_driver or request.user.is_staff
        )

class OwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
            return bool(
                request.method in SAFE_METHODS or
                request.user.is_authenticated and obj.user == request.user or request.user.is_authenticated and request.user.is_staff
            )