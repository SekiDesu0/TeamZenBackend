from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Team

class IsAdminOrReadOnly(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsTeamManager(BasePermission):
    """
    Allows access only to team managers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'MANAGER'

class IsOwnerOrTeamManager(BasePermission):
    """
    Allows access to an object only if the user is the owner of the object or a manager of the team.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'ADMIN':
            return True
        if obj.user == request.user:
            return True
        if request.user.role == 'MANAGER':
            # Check if the user (obj) is in a team managed by the request.user
            for team in Team.objects.filter(manager=request.user):
                if obj.user in team.members.all():
                    return True
        return False

class IsTeamMember(BasePermission):
    """
    Allows read-only access to users who are in the same team.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # Check if the user (obj) is in the same team as the request.user
            for team in Team.objects.filter(members=request.user):
                if obj in team.members.all():
                    return True
        return False
