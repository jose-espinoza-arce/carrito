# -*- coding: utf-8 -*-
from dashboard.cmproducts.models import TequilaType, EventType, BoxPresentation, Template, CustomImage, Tag
from dashboard.cmproducts.serializers import TequilaTypeSerializer, \
    EventTypeSerializer, BoxPresentationSerializer, \
    TemplateSerializer, CustomImageSerializer, TagSerializer

from catalogue.models import ProductClass, Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from django.views import generic
from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

import json
from django.shortcuts import render_to_response
from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView

#from cmproducts.models import TequilaType


#-----------------FORMS---------
class EventForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = '__all__'


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = '__all__'

#----------------------------------------------

class TemplateView(generic.FormView):

    success_url = '/dashboard/'

    template_name = 'cmproducts/types.html'
    form_class = TemplateForm
    #model = TequilaType

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.save()

        return super(TemplateView, self).form_valid(form)

@csrf_exempt
def TagBlob(request):
    if request.method == 'POST':
        #base64_string = request.order
        #print base64_string
        print request.is_ajax()
        data = json.loads(request.body)
        serializer = TagSerializer(data=data['item'])

        #print data['item']['tag']
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        #serializer.
        #print serializer.to_internal_value(data=data['item'])

        return HttpResponse('<h1>Image successfully saved!</h1>')



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TequilaTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductClass.objects.all()
    serializer_class = TequilaTypeSerializer



class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class BoxPresentationViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = BoxPresentationSerializer

    def list(self, request, type_pk=None, *args, **kwargs):
        if type_pk:
            queryset = self.queryset.filter(product_class_id=type_pk)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def list(self, request, event_pk=None, *args, **kwargs):
        if event_pk:
            queryset = self.queryset.filter(etype=event_pk)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CustomImageViewSet(viewsets.ModelViewSet):
    queryset = CustomImage.objects.all()
    serializer_class = CustomImageSerializer

    def create(self, request, *args, **kwargs):
        print 'Request Data:'
        print request.data
        serializer = self.get_serializer(data=request.data)

        ser = serializer.is_valid(raise_exception=True)
        print 'Serializer:'
        #print serializer.data
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


#-------------------------------------------------------------------------------------

class EventCreateView(generic.CreateView):
    template_name = 'dashboard/cmproducts/event_form.html'
    model = EventType
    form_class = EventForm

    def get_context_data(self, **kwargs):
        ctx = super(EventCreateView, self).get_context_data(**kwargs)
        ctx['title'] = "Añadir un nuevo evento"
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Nuevo evento creado"))
        return reverse("dashboard:event-list")


class EventListView(generic.ListView):
    template_name = 'dashboard/cmproducts/event_list.html'
    context_object_name = 'classes'
    model = EventType

    def get_context_data(self, *args, **kwargs):
        ctx = super(EventListView, self).get_context_data(*args, **kwargs)
        ctx['title'] = _("Events")
        return ctx


class EventUpdateView(generic.UpdateView):
    template_name = 'dashboard/cmproducts/event_form.html'
    model = EventType
    form_class = EventForm

    def get_context_data(self, **kwargs):
        ctx = super(EventUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Actualizar evento '%s'") % self.object.name
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Product type update successfully"))
        return reverse("dashboard:event-list")


class EventDeleteView(generic.DeleteView):
    template_name = 'dashboard/cmproducts/event_delete.html'
    model = EventType
    form_class = EventForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(EventDeleteView, self).get_context_data(*args, **kwargs)
        ctx['title'] = _("Eliminar evento '%s'") % self.object.name
        #product_count = self.object.products.count()

        #if product_count > 0:
        #    ctx['disallow'] = True
        #    ctx['title'] = _("Unable to delete '%s'") % self.object.name
        #    messages.error(self.request,
        #                   _("%i products are still assigned to this type") %
        #                   product_count)
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Evento eliminado"))
        return reverse("dashboard:event-list")



class TemplateCreateView(generic.CreateView):
    template_name = 'dashboard/cmproducts/template_form.html'
    model = Template
    form_class = TemplateForm

    def get_context_data(self, **kwargs):
        ctx = super(TemplateCreateView, self).get_context_data(**kwargs)
        ctx['title'] = "Añadir una plantilla nueva"
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Nueva plantilla creada"))
        return reverse("dashboard:template-list")


class TemplateListView(generic.ListView):
    template_name = 'dashboard/cmproducts/template_list.html'
    context_object_name = 'classes'
    model = Template

    def get_context_data(self, *args, **kwargs):
        ctx = super(TemplateListView, self).get_context_data(*args, **kwargs)
        ctx['title'] = _("Plantillas")
        return ctx


class TemplateUpdateView(generic.UpdateView):
    template_name = 'dashboard/cmproducts/template_form.html'
    model = Template
    form_class = TemplateForm

    def get_context_data(self, **kwargs):
        ctx = super(TemplateUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Actualizar plantilla '%s'") % self.object.name
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Plantilla actualizada"))
        return reverse("dashboard:template-list")


class TemplateDeleteView(generic.DeleteView):
    template_name = 'dashboard/cmproducts/template_delete.html'
    model = Template
    form_class = TemplateForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(TemplateDeleteView, self).get_context_data(*args, **kwargs)
        ctx['title'] = _("Eliminar plantilla '%s'") % self.object.name
        #product_count = self.object.products.count()

        #if product_count > 0:
        #    ctx['disallow'] = True
        #    ctx['title'] = _("Unable to delete '%s'") % self.object.name
        #    messages.error(self.request,
        #                   _("%i products are still assigned to this type") %
        #                   product_count)
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Plantilla eliminada"))
        return reverse("dashboard:template-list")

