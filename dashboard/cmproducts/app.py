from django.conf.urls import url

from oscar.core.application import Application
from oscar.core.loading import get_class

from dashboard.cmproducts.views import TemplateView, TemplateCreateView, TemplateListView, TemplateUpdateView, TemplateDeleteView, EventCreateView, EventListView, EventUpdateView, EventDeleteView

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
            #url(r'^plantillas/$',  TemplateView.as_view(), name='plantilla'),
            url(r'^evento/crear/$',
                EventCreateView.as_view(),
                name='event-create'),
            url(r'^eventos/$',
                EventListView.as_view(),
                name='event-list'),
            url(r'^evento/(?P<pk>\d+)/actualizar/$',
                EventUpdateView.as_view(),
                name='event-update'),
            url(r'^evento/(?P<pk>\d+)/eliminar/$',
                EventDeleteView.as_view(),
                name='event-delete'),
            url(r'^plantilla/crear/$',
                TemplateCreateView.as_view(),
                name='template-create'),
            url(r'^plantillas/$',
                TemplateListView.as_view(),
                name='template-list'),
            url(r'^plantilla/(?P<pk>\d+)/actualizar/$',
                TemplateUpdateView.as_view(),
                name='template-update'),
            url(r'^plantilla/(?P<pk>\d+)/eliminar/$',
                TemplateDeleteView.as_view(),
                name='template-delete'),

        ]
        return self.post_process_urls(urls)


application = CmproductApplication()
