from xml.etree.ElementInclude import include
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import SurveyViewSet

router = SimpleRouter()
router.register('', SurveyViewSet)

urlpatterns = [
    path('', include(router.urls), name='survey-viewset-routes'),
]