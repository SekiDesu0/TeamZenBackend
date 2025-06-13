from rest_framework import serializers
from .models import User, Team, TeamMembership, MBIForm, Organization, Prediction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'default': True}
        }

    def create(self, validated_data):
        #print(">>> VALIDATED:", validated_data)  # Add this
        
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)      #hashes the password
        user.is_active = True            #activates user
        user.save()
        return user

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'created_at']

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

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['id', 'mbi_form', 'burnout_level', 'prediction_score', 'created_at', 'model_version']
        read_only_fields = ['created_at', 'model_version']
