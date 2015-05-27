# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmproducts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='etype',
            field=models.ForeignKey(related_name='templates', default=1, verbose_name=b'Tipo de evento', to='cmproducts.EventType'),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=60, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='template',
            name='timage',
            field=models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/templates/', verbose_name=b'Plantilla'),
        ),
    ]
