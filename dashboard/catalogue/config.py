# from django.apps import AppConfig
# from django.utils.translation import ugettext_lazy as _
#
#
# class CatalogueDashboardConfig(AppConfig):
#     label = 'catalogue_dashboard'
#     name = 'dashboard.catalogue'
#     verbose_name = _('Catalogue')


from oscar.apps.dashboard.catalogue import config


class CatalogueDashboardConfig(config.CatalogueDashboardConfig):
    label = 'catalogue_dashboard'
    name = 'dashboard.catalogue'