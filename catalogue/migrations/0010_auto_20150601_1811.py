# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20150529_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_original_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/media/generic_profile_image.png', upload_to=b'images/catalogue/product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_tag',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/media/generic_profile_image.png', upload_to=b'images/catalogue/product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_zoom_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/media/generic_profile_image.png', upload_to=b'images/catalogue/product'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category',
            field=models.ForeignKey(verbose_name='Category', to='catalogue.Category'),
        ),
        migrations.AlterField(
            model_name='productclass',
            name='bimage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/catalogo/', verbose_name=b'Imagen'),
        ),
    ]
