# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='patronymic',
            field=models.CharField(max_length=100),
        ),
    ]
