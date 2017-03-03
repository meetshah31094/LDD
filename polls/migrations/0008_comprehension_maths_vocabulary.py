# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-10 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_pythonquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='comprehension',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('all_id', models.IntegerField(blank=True, null=True)),
                ('std', models.IntegerField(blank=True, null=True)),
                ('q_text', models.TextField(blank=True, null=True)),
                ('option1', models.TextField(blank=True, null=True)),
                ('option2', models.TextField(blank=True, null=True)),
                ('option3', models.TextField(blank=True, null=True)),
                ('option4', models.TextField(blank=True, null=True)),
                ('ans', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='maths',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('all_id', models.IntegerField(blank=True, null=True)),
                ('std', models.IntegerField(blank=True, null=True)),
                ('q_text', models.TextField(blank=True, null=True)),
                ('option1', models.TextField(blank=True, null=True)),
                ('option2', models.TextField(blank=True, null=True)),
                ('option3', models.TextField(blank=True, null=True)),
                ('option4', models.TextField(blank=True, null=True)),
                ('ans', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('all_id', models.IntegerField(blank=True, null=True)),
                ('std', models.IntegerField(blank=True, null=True)),
                ('q_text', models.TextField(blank=True, null=True)),
                ('option1', models.TextField(blank=True, null=True)),
                ('option2', models.TextField(blank=True, null=True)),
                ('option3', models.TextField(blank=True, null=True)),
                ('option4', models.TextField(blank=True, null=True)),
                ('ans', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
