from rest_framework import permissions


class IsReadOnlyOperation(permissions.BasePermission):
    # permissions.SAFE_METHODS = ('GET', 'OPTIONS', 'HEAD')
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False
