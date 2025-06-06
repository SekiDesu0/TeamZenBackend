from rest_framework import serializers
from .models import User, Team, TeamMembership, MBIForm, Organization

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'organization', 'manager']

class TeamMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = ['id', 'user', 'team', 'joined_at']

class MBIFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MBIForm
        fields = [
            'id', 'user', 'team', 'submitted_at',
            'emotional_exhaustion', 'depersonalization',
            'personal_accomplishment', 'raw_answers'
        ]

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'created_at']