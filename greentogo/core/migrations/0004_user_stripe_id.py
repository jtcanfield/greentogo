# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170729_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]