# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 10:58
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_spot_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='valid_status',
            field=django_fsm.FSMField(default='not_valid', max_length=50),
            preserve_default=False,
        ),
    ]
