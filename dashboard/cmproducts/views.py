from dashboard.cmproducts.models import TequilaType, EventType, BoxPresentation, Template, CustomImage
from dashboard.cmproducts.serializers import TequilaTypeSerializer, EventTypeSerializer, BoxPresentationSerializer, TemplateSerializer, CustomImageSerializer

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from django.views import generic
from django import forms
from django.shortcuts import render_to_response
from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView

#from cmproducts.models import TequilaType

class PlantillaForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = '__all__'



class PlantillaView(generic.FormView):

    success_url = '/dashboard/'

    template_name = 'cmproducts/types.html'
    form_class = PlantillaForm
    #model = TequilaType

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.save()

        return super(PlantillaView, self).form_valid(form)


class TequilaTypeViewSet(viewsets.ModelViewSet):
    queryset = TequilaType.objects.all()
    serializer_class = TequilaTypeSerializer



class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class BoxPresentationViewSet(viewsets.ModelViewSet):
    queryset = BoxPresentation.objects.all()
    serializer_class = BoxPresentationSerializer

    def list(self, request, size_pk=None, *args, **kwargs):
        if size_pk:
            queryset = self.queryset.filter(type_id=size_pk)
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
