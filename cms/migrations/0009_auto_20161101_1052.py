# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_remove_paper_recommended'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='note',
            field=models.CharField(blank=True, max_length=255, verbose_name='Note'),
        ),
        migrations.AddField(
            model_name='report',
            name='grade',
            field=models.CharField(blank=True, max_length=32, verbose_name='Grade'),
        ),
    ]
