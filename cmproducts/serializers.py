from cmproducts.models import TequilaType, EventType, BoxPresentation, Template, CustomImage
from basket.models import Basket, Line
from rest_framework import serializers


class TequilaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TequilaType
        fields = ('id', 'name', 'bimage', 'maskimage',)


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'name', 'etype', 'timage',)


class EventTypeSerializer(serializers.ModelSerializer):
    #templates = TemplateSerializer(many=True, read_only=True)

    class Meta:
        model = EventType
        fields = ('id', 'name',)# 'templates',)


class BoxPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxPresentation
        fields = ('id', 'type', 'bottlesize', 'bottles',
                  'maxlabels', 'bottlerow', 'img_original_size',
                  'img_zoom_size', 'img_tag'
        )


class CustomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomImage
        fields = ('id', 'file', 'name')

