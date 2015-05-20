# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoxPresentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bottlesize', models.CharField(max_length=20)),
                ('bottles', models.PositiveSmallIntegerField()),
                ('maxlabels', models.PositiveSmallIntegerField()),
                ('bottlerow', models.PositiveSmallIntegerField()),
                ('img_original_size', models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/boxpresentation/')),
                ('img_zoom_size', models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/boxpresentation/')),
                ('img_tag', models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/boxpresentation/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/custom/')),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('timage', models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/templates/')),
                ('etype', models.ForeignKey(related_name='templates', default=1, to='cmproducts.EventType')),
            ],
        ),
        migrations.CreateModel(
            name='TequilaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('bimage', models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/tequila/')),
                ('maskimage', models.ImageField(default=b'/home/jose/dev/djangodev/carrito/maravatioapp/static/generic_profile_image.png', upload_to=b'images/tequila/')),
            ],
        ),
        migrations.AddField(
            model_name='boxpresentation',
            name='type',
            field=models.ForeignKey(related_name='sizes', default=1, to='cmproducts.TequilaType'),
        ),
    ]
