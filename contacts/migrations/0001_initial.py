# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstName', models.CharField(max_length=25, blank=True)),
                ('lastName', models.CharField(max_length=25, blank=True)),
                ('email', models.EmailField(null=True, unique=True, max_length=70, blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{6,15}$')])),
                ('date_created', models.DateField(verbose_name='Created on date', auto_now_add=True)),
                ('created_by', models.ForeignKey(verbose_name='contact_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
