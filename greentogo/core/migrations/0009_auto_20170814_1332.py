# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 13:32
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_locationstockcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationstockcount',
            name='location',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='stock_counts',
                to='core.Location'
            ),
        ),
        migrations.AlterField(
            model_name='unclaimedsubscription',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='unclaimedsubscription',
            unique_together=set([('email', 'plan')]),
        ),
    ]
