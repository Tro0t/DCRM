# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-04 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0003_sitepreferences'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SitePreferences',
            new_name='Setting',
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
    ]
