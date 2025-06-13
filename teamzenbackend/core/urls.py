from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, TeamMembershipViewSet, MBIFormViewSet, OrganizationViewSet, PredictionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'team-memberships', TeamMembershipViewSet)
router.register(r'mbi-forms', MBIFormViewSet)
router.register(r'predictions', PredictionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
