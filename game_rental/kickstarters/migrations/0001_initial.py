# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KickStarter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('kickstarter_id', models.CharField(max_length=50, unique=True)),
                ('category_id', models.CharField(max_length=5)),
            ],
        ),
    ]
