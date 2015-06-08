# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_auto_20150601_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='tag_img',
            field=models.ImageField(default=b'images/catalogo/generic_profile_image.png', upload_to=b'images/catalogo/', verbose_name=b'Imagen'),
        ),
        migrations.AlterField(
            model_name='productclass',
            name='bimage',
            field=models.ImageField(default=b'images/catalogo/generic_profile_image.png', upload_to=b'images/catalogo/', verbose_name=b'Imagen'),
        ),
    ]
