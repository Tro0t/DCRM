# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-05 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0008_auto_20170105_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='package',
            field=models.CharField(help_text='Unique identifier.<br />Example: com.darwindev.xxtouch', max_length=255, unique=True, verbose_name='Package'),
        ),
        migrations.AlterField(
            model_name='version',
            name='download_times',
            field=models.IntegerField(default=0, verbose_name='Download Times'),
        ),
        migrations.AlterField(
            model_name='version',
            name='md5',
            field=models.CharField(default='', max_length=32, verbose_name='MD5'),
        ),
        migrations.AlterField(
            model_name='version',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WEIPDCRM.Package'),
        ),
        migrations.AlterField(
            model_name='version',
            name='sha1',
            field=models.CharField(default='', max_length=40, verbose_name='SHA1'),
        ),
        migrations.AlterField(
            model_name='version',
            name='sha256',
            field=models.CharField(default='', max_length=64, verbose_name='SHA256'),
        ),
        migrations.AlterField(
            model_name='version',
            name='size',
            field=models.BigIntegerField(default=0, verbose_name='Size'),
        ),
    ]
