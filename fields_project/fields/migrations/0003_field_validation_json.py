# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_fieldoptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='validation_json',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
