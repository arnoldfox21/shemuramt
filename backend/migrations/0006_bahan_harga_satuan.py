# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_pembelian'),
    ]

    operations = [
        migrations.AddField(
            model_name='bahan',
            name='harga_satuan',
            field=models.IntegerField(null=True),
        ),
    ]