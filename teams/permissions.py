from rest_framework import permissions


class IsCoach(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_coach():
            return True

    def has_object_permission(self, request, view, obj):
        if obj.coach.pk == request.user.pk:
            return True
        return False


class IsPlayer(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_player():
            return True
