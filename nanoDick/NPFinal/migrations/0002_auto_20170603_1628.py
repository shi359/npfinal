# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 16:28
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NPFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hash_tag',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=['no Tag']),
        ),
    ]
