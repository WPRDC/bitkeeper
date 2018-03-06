# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-06 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitkeeper', '0024_auto_20180306_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipality',
            name='state_house_district',
        ),
        migrations.AddField(
            model_name='municipality',
            name='state_house_district',
            field=models.ManyToManyField(blank=True, to='bitkeeper.StateHouseDistrict', verbose_name='state House district'),
        ),
        migrations.RemoveField(
            model_name='municipality',
            name='state_senate_district',
        ),
        migrations.AddField(
            model_name='municipality',
            name='state_senate_district',
            field=models.ManyToManyField(blank=True, to='bitkeeper.StateSenateDistrict', verbose_name='state Senate district'),
        ),
    ]
