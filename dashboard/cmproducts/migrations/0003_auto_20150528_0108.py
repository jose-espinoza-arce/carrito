# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmproducts', '0002_auto_20150527_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxpresentation',
            name='img_original_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/generic_profile_image.png', upload_to=b'images/boxpresentation/'),
        ),
        migrations.AlterField(
            model_name='boxpresentation',
            name='img_tag',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/generic_profile_image.png', upload_to=b'images/boxpresentation/'),
        ),
        migrations.AlterField(
            model_name='boxpresentation',
            name='img_zoom_size',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/generic_profile_image.png', upload_to=b'images/boxpresentation/'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='file',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/generic_profile_image.png', upload_to=b'images/custom/'),
        ),
        migrations.AlterField(
            model_name='template',
            name='timage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/generic_profile_image.png', upload_to=b'images/templates/', verbose_name=b'Plantilla'),
        ),
        migrations.AlterField(
            model_name='tequilatype',
            name='bimage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/generic_profile_image.png', upload_to=b'images/tequila/'),
        ),
        migrations.AlterField(
            model_name='tequilatype',
            name='maskimage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatiomaster/static/generic_profile_image.png', upload_to=b'images/tequila/'),
        ),
    ]
