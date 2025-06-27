from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TeamMembership

@receiver(post_save, sender=TeamMembership)
def add_user_to_team_members(sender, instance, created, **kwargs):
    if created:
        instance.team.members.add(instance.user)
