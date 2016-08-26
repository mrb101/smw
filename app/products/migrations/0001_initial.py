# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
