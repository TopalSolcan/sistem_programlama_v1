# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-19 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
