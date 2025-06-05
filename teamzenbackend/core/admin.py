from django.contrib import admin
from .models import User, Organization, Team, TeamMembership, MBIForm, Prediction, ExternalActivity

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(TeamMembership)
admin.site.register(MBIForm)
admin.site.register(Prediction)
admin.site.register(ExternalActivity)