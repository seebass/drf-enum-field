from rest_framework.viewsets import ModelViewSet

from .models import TestResource
from .serializers import TestResourceSerializer


class TestResourceViewSet(ModelViewSet):
    serializer_class = TestResourceSerializer
    queryset = TestResource.objects.all()
