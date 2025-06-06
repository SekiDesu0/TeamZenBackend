from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Team, TeamMembership, MBIForm, Organization
from .serializers import UserSerializer, TeamSerializer, TeamMembershipSerializer, MBIFormSerializer, OrganizationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

class TeamMembershipViewSet(viewsets.ModelViewSet):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer
    permission_classes = [IsAuthenticated]

class MBIFormViewSet(viewsets.ModelViewSet):
    queryset = MBIForm.objects.all()
    serializer_class = MBIFormSerializer
    permission_classes = [IsAuthenticated]
    
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
