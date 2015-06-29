from enumfields.fields import EnumField
from rest_framework.fields import ChoiceField

from drf_enum_field.fields import EnumField as RestEnumField


class EnumFieldSerializerMixin(object):
    def build_standard_field(self, field_name, model_field):
        field_class, field_kwargs = super(EnumFieldSerializerMixin, self).build_standard_field(field_name, model_field)
        if field_class == ChoiceField and isinstance(model_field, EnumField):
            field_class = RestEnumField
            field_kwargs['enum_type'] = model_field.enum
        return field_class, field_kwargs
