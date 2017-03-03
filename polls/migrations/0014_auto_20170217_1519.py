# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_question_standard'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('all_id', models.IntegerField(blank=True, null=True)),
                ('std', models.IntegerField(blank=True, null=True)),
                ('pic', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.DeleteModel(
            name='studentprof',
        ),
    ]