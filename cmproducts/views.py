from cmproducts.models import TequilaType, EventType, BoxPresentation, Template, CustomImage
from cmproducts.serializers import TequilaTypeSerializer, EventTypeSerializer, BoxPresentationSerializer, TemplateSerializer, CustomImageSerializer

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response



class TequilaTypeViewSet(viewsets.ModelViewSet):
    queryset = TequilaType.objects.all()
    serializer_class = TequilaTypeSerializer



class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class BoxPresentationViewSet(viewsets.ModelViewSet):
    queryset = BoxPresentation.objects.all()
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
