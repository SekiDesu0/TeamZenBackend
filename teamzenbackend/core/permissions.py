from rest_framework.permissions import BasePermission

class IsTeamManager(BasePermission):
    """
    Allows access only to managers of the team.
    """

    def has_permission(self, request, view):
        # Allow read-only access for authenticated users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.is_authenticated

        # For write operations, check if the user is a manager of the target team
        return request.user.role == 'MANAGER'

    def has_object_permission(self, request, view, obj):
        """
        Called when modifying specific objects.
        obj is a User instance being accessed or modified.
        """
        if request.user.role == 'ADMIN':
            return True

        if request.user.role != 'MANAGER':
            return False

        # # Check if the user (obj) belongs to a team managed by the request.user
        # managed_teams = request.user.managed_teams.all()
        # for team in managed_teams:
        #     if obj in team.members.all():
        #         return True

        return False
