# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
