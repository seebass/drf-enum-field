from rest_framework.serializers import ModelSerializer
from drf_enum_field.serializers import EnumFieldSerializerMixin
from .models import TestResource


class TestResourceSerializer(EnumFieldSerializerMixin, ModelSerializer):
    class Meta:
        model = TestResource
