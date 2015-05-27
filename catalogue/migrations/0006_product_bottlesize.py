# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20150527_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bottlesize',
            field=models.CharField(default='3 L', max_length=20),
            preserve_default=False,
        ),
    ]
