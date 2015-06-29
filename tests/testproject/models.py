from django.db import models
from enumfields import Enum, EnumField


class TestResource(models.Model):
    class Type(Enum):
        DEFAULT = 'DEFAULT'
        NON_DEFAULT = 'NON_DEFAULT'

    type = EnumField(Type)
    name = models.CharField(max_length=255)
