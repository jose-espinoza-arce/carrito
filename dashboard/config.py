from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

#from oscar.apps.dashboard import config


class DashboardConfig(AppConfig):
    label = 'dashboarddi'
    name = 'dashboard'
    verbose_name = _('Dashboard')