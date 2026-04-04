from rest_framework.permissions import BasePermission,SAFE_METHODS



class IsAdminOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        
        return user.is_superuser
    
    def has_permission(self, request, view):
        user = request.user
        
        if request.method in SAFE_METHODS:
            return True

        return user.is_superuser


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj.author
    
    def has_permission(self, request, view):
        return True
    




    