from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of a book to modify or delete it.
    Unauthenticated users and non-owners are allowed read-only access (GET, HEAD, OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only granted if request.user matches the object's owner
        return obj.owner == request.user
