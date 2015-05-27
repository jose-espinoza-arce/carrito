from django.conf.urls import include, url
#from django.contrib import admin
from dashboard.cmproducts.views import TequilaTypeViewSet, EventTypeViewSet, \
                            BoxPresentationViewSet, TemplateViewSet, CustomImageViewSet
from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework_nested import routers as drf_routers

#from django.conf import settings
#from django.conf.urls.static import static





primary_router = drf_routers.SimpleRouter()
primary_router.register(r'events', EventTypeViewSet)
primary_router.register(r'types', TequilaTypeViewSet)

secondary_router_events = drf_routers.NestedSimpleRouter(primary_router, r'events', lookup='event')
secondary_router_events.register(r'templates', TemplateViewSet)
secondary_router_types = drf_routers.NestedSimpleRouter(primary_router, r'types', lookup='size')
secondary_router_types.register(r'sizes', BoxPresentationViewSet)


router = routers.DefaultRouter()
router.register('types', TequilaTypeViewSet)
router.register('events', EventTypeViewSet)
router.register('sizes', BoxPresentationViewSet)
router.register('templates', TemplateViewSet)
router.register('customimages', CustomImageViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'djmaravtio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', PlantillaView.as_view(), name='plantilla'),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(primary_router.urls)),
    url(r'^api/', include(secondary_router_events.urls)),
    url(r'^api/', include(secondary_router_types.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

