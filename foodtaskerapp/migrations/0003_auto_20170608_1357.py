# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-08 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0002_customer_driver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='avartar',
            new_name='avatar',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='avartar',
            new_name='avatar',
        ),
    ]
