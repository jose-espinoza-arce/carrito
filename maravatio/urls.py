from django.conf.urls import patterns, include, url
from django.contrib import admin
from oscar.app import application

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
)
