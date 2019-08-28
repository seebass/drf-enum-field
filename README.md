drf-enum-field
==============
Extension for Django REST Framework 3 which allows for using EnumField from https://github.com/hzdg/django-enumfields.

## Setup ##

	pip install drf-enum-field

## Requirements ##

* Python 2.7+
* Django 1.6+
* Django REST Framework 3.9
* django-enumfields 0.9+

## Features ##

By using the **EnumFieldSerializerMixin** EnumFields are serialized and deserialized correctly.

## Example ##

### Model ###

	class TestResource(models.Model):
    	class Type(Enum):
        	DEFAULT = 'DEFAULT'
        	NON_DEFAULT = 'NON_DEFAULT'

    	type = EnumField(Type)
    	name = models.CharField(max_length=255)

### Serializer ###

	class TestResourceSerializer(EnumFieldSerializerMixin, ModelSerializer):
			class Meta:
        		model = TestResource

### View ###

	class TestResourceViewSet(ModelViewSet):
    	serializer_class = TestResourceSerializer
    	queryset = TestResource.objects.all()

### Result ###

		{
			"id": 1,
			"name": "Test-Resource",
			"type": "DEFAULT"
		}
