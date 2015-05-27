# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20150527_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bottlerow',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='bottles',
            field=models.PositiveSmallIntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='img_original_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/catalogue/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_tag',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/catalogue/product'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_zoom_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/catalogue/product'),
        ),
        migrations.AddField(
            model_name='product',
            name='maxlabels',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
    ]
