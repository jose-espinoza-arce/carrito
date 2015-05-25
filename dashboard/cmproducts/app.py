from django.conf.urls import url

from oscar.core.application import Application
from oscar.core.loading import get_class

from dashboard.cmproducts.views import PlantillaView

class CmproductApplication(Application):
    name = None

    default_permissions = ['is_staff', ]
    permissions_map = _map = {
        'catalogue-product': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-create': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-list': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-delete': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-lookup': (['is_staff'],
                                     ['partner.dashboard_access']),
    }

    #cmproduct_view = get_class('dashboard.cmproduct.views',
     #                             'PlantillaView')


    def get_urls(self):
        urls = [
            url(r'^plantillas/$',
                PlantillaView.as_view(),
                name='plantilla'),
        ]
        return self.post_process_urls(urls)


application = CmproductApplication()
