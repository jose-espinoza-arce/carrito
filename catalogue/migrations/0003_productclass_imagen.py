# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_product_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='imagen',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/catalogo/'),
        ),
    ]
