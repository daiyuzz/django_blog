# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-17 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200117_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
