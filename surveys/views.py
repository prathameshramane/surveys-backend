from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Survey
from .serializers import SurveySerializer

# Create your views here.
class SurveyViewSet(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [AllowAny, ]
