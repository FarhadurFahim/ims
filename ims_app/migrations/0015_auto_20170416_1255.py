# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims_app', '0014_auto_20170416_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockout',
            name='stock_in_info',
        ),
        migrations.AddField(
            model_name='stockout',
            name='product_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ims_app.Stocks'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockout',
            name='product_sell_unit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
