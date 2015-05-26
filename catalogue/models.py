import os
from django.conf import settings

from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractProductClass


class Product(AbstractProduct):
    event_type = models.TextField(max_length=255, default='Fiesta')


class ProductClass(AbstractProductClass):
    imagen = models.ImageField(
        upload_to='images/catalogo/',
        default=os.path.join(settings.STATIC_ROOT,'generic_profile_image.png'),
        )

from oscar.apps.catalogue.models import *