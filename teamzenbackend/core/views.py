from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Team, TeamMembership, MBIForm, Organization, Prediction
from .serializers import UserSerializer, TeamSerializer, TeamMembershipSerializer, MBIFormSerializer, OrganizationSerializer, PredictionSerializer
from .permissions import IsAdminOrReadOnly, IsTeamManager, IsOwnerOrTeamManager, IsTeamMember

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly | IsTeamManager | IsOwnerOrTeamManager | IsTeamMember]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return User.objects.all()
        elif user.role == 'MANAGER':
            return User.objects.filter(teams__in=user.managed_teams.all()).distinct()
        else:
            return User.objects.filter(teams__in=user.teams.all()).distinct()
    
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly | IsTeamManager]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return Team.objects.all()
        elif user.role == 'MANAGER':
            return user.managed_teams.all()
        else:
            return user.teams.all()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role == 'MANAGER':
            serializer.save(manager=user)
        elif user.role == 'ADMIN':
            serializer.save()

class TeamMembershipViewSet(viewsets.ModelViewSet):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly | IsTeamManager]

class MBIFormViewSet(viewsets.ModelViewSet):
    queryset = MBIForm.objects.all()
    serializer_class = MBIFormSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrTeamManager]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return MBIForm.objects.all()
        elif user.role == 'MANAGER':
            return MBIForm.objects.filter(team__in=user.managed_teams.all())
        else:
            return MBIForm.objects.filter(user=user)

class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly | IsTeamManager]
