# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmproducts', '0005_auto_20150601_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='uploadimage',
            field=models.ForeignKey(default=1, to='cmproducts.CustomImage'),
        ),
    ]
