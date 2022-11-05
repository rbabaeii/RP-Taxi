from rest_framework.permissions import BasePermission,SAFE_METHODS

class Is_StaffOrAdminReadonly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and request.user.is_superuser or
            request.user.is_staff
        )
class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)    


class IsSuperUserOrAuthentication(BasePermission):

    def has_permission(self, request, view):
        return bool(
             (request.user.is_authenticated and request.user.is_superuser) or
             (request.user.is_authenticated ) 
        ) 


