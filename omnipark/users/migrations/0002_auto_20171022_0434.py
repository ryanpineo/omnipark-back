# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vd_card_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='vop_card_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
