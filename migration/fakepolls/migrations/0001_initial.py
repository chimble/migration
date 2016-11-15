# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('type_text', models.CharField(max_length=200)),
                ('color_text', models.CharField(max_length=200)),
                ('cmc_num', models.IntegerField(default=0)),
                ('rarity_text', models.CharField(max_length=200)),
                ('price_num', models.FloatField(default=0)),
                ('artist_text', models.CharField(max_length=200)),
                ('cardset_text', models.CharField(max_length=200)),
            ],
        ),
    ]