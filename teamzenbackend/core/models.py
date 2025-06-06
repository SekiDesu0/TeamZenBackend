from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('MEMBER', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')
    is_active = models.BooleanField(default=True)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'MANAGER'})

class TeamMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class MBIForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    emotional_exhaustion = models.IntegerField()
    depersonalization = models.IntegerField()
    personal_accomplishment = models.IntegerField()
    raw_answers = models.JSONField(null=True, blank=True)

class Prediction(models.Model):
    mbi_form = models.OneToOneField(MBIForm, on_delete=models.CASCADE)
    burnout_level = models.CharField(max_length=20)
    prediction_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    model_version = models.CharField(max_length=50)

class ExternalActivity(models.Model):
    SOURCE_CHOICES = (
        ('GOOGLE_CALENDAR', 'Google Calendar'),
        ('JIRA', 'Jira'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=30, choices=SOURCE_CHOICES)
    data = models.JSONField()
    collected_at = models.DateTimeField()