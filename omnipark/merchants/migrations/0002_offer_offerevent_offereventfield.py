# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('community_code', models.CharField(max_length=255)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='merchants.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='OfferEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='merchants.Offer')),
            ],
        ),
        migrations.CreateModel(
            name='OfferEventField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='merchants.OfferEvent')),
            ],
        ),
    ]
