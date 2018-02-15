# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-14 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitkeeper', '0014_remove_firedepartment_council_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emsdepartment',
            name='council_district',
        ),
        migrations.RemoveField(
            model_name='policedepartment',
            name='council_district',
        ),
        migrations.AddField(
            model_name='pghcouncildistrict',
            name='ems_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bitkeeper.EMSDepartment', verbose_name='EMS department'),
        ),
    ]