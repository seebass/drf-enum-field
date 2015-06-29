# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enumfields.fields
from ..models import TestResource


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', enumfields.fields.EnumField(max_length=10, enum=TestResource.Type)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
