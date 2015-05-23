from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    event_type = models.TextField(max_length=255, default='Fiesta')


from oscar.apps.catalogue.models import *