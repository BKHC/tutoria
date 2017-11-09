# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(upload_to=students.models.user_directory_path),
        ),
    ]