# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_composition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composition',
            name='ans',
        ),
    ]
