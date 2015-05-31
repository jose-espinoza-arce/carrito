# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20150528_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_original_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/media/generic_profile_image.png', upload_to=b'images/catalogue/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_tag',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/media/generic_profile_image.png', upload_to=b'images/catalogue/product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_zoom_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/media/generic_profile_image.png', upload_to=b'images/catalogue/product'),
        ),
    ]
