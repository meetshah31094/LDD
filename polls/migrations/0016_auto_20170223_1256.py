# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.ImageField(upload_to=b'documents/%Y/%m/%d'),
        ),
    ]
