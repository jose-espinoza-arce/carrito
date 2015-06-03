from dashboard.cmproducts.models import TequilaType, EventType, BoxPresentation, Template, CustomImage, Tag
from catalogue.models import ProductClass, Product

from oscar.apps.partner.models import StockRecord

from rest_framework import serializers


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        print 'to internal value'
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class TagSerializer(serializers.ModelSerializer):
    tag = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Tag
        fields = ('id', 'name', 'tag')


class TequilaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClass
        fields = ('id', 'name', 'bimage', 'track_stock')


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

class StockRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRecord
        #fields = '__all__'


class CustomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomImage
        fields = ('id', 'file', 'name')