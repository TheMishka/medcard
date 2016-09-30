# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('emailType', models.CharField(choices=[('p', 'Личный'), ('w', 'Рабочий'), ('o', 'Другой')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский')], max_length=1)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HumanDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(max_length=20)),
                ('document_number', models.PositiveIntegerField()),
                ('document_date', models.DateField()),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medcard.Human')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=20)),
                ('phoneType', models.CharField(choices=[('m', 'Сотовый'), ('w', 'Рабочий'), ('o', 'Другой')], max_length=1)),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medcard.Human')),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='human',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medcard.Human'),
        ),
    ]
