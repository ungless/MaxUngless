# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_topic_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
    ]