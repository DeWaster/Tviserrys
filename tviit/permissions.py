from rest_framework import permissions


class IsSender(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the snippet.
        return obj.sender == request.user