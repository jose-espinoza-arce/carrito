# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_product_bottlesize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bottlerow',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='bottles',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='bottlesize',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='maxlabels',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
