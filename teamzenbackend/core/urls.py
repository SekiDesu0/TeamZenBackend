from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, TeamMembershipViewSet, MBIFormViewSet, OrganizationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'team-memberships', TeamMembershipViewSet)
router.register(r'mbi-forms', MBIFormViewSet)
router.register(r'organizations', OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
