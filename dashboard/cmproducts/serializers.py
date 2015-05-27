from dashboard.cmproducts.models import TequilaType, EventType, BoxPresentation, Template, CustomImage
from catalogue.models import ProductClass, Product
from rest_framework import serializers


class TequilaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClass
        fields = ('id', 'name', 'bimage',)


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
        model = Product
        fields = ('id', 'product_class', 'categories', 'bottlesize', 'bottles',
                  'maxlabels', 'bottlerow', 'img_original_size',
                  'img_zoom_size', 'img_tag'
        )


class CustomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomImage
        fields = ('id', 'file', 'name')