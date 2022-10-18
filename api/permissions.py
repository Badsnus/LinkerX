from rest_framework.permissions import BasePermission, IsAdminUser


class IsOwnerOfLink(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or IsAdminUser()
