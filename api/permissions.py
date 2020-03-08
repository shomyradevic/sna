from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):

    def generate_error_message(self, entity: str) -> dict:
        entity = entity.lower()
        message = 'You can not edit other user '
        if entity != 'user':
            message += entity + ' '
        message += 'unless you have administrative privileges!'
        return {'message': message}

    def has_object_permission(self, request, obj, view=None):
        if request.user == obj or request.user.is_staff:
            return True
        return False