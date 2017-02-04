# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 19:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('core', '0001_initial'), ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('uuid', models.UUIDField(
                    primary_key=True, serialize=False)),
                ('service', models.CharField(
                    choices=[('IN', 'Check in'), ('OUT', 'Check out')],
                    max_length=25)),
            ], ),
        migrations.CreateModel(
            name='LocationTag',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='core.Location')),
                ('subscription', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='core.Subscription')),
            ], ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('code', models.CharField(
                    help_text='Code must be capital letters and numbers with no spaces.',
                    max_length=25,
                    unique=True,
                    validators=[
                        django.core.validators.RegexValidator('^[A-Z0-9]$')
                    ])),
                ('description', models.CharField(max_length=255)),
                ('number_of_boxes', models.PositiveIntegerField(
                    blank=True, null=True)),
            ], ),
    ]
