from django.urls.conf import include, path
from rest_framework.routers import SimpleRouter

from polls.views import SubjectModelViewSet

router = SimpleRouter()
router.register('subject', SubjectModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
