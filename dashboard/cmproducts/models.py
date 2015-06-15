from django.db import models
from django.conf import settings
import os

import StringIO
from PIL import Image


class Tag(models.Model):
    name = models.CharField(max_length=60, blank=True)
    uploadimage = models.ForeignKey('CustomImage', default=1)
    label = models.ImageField(
        upload_to='images/tags/',
        default='images/generic_image.png',
    )

    def __unicode__(self):
        return self.name


class TequilaType(models.Model):
    name = models.CharField(max_length=60)
    bimage = models.ImageField(
        upload_to='images/tequila/',
        default=os.path.join(settings.MEDIA_ROOT,'generic_profile_image.png'),
    )
    maskimage = models.ImageField(
        upload_to='images/tequila/',
        default=os.path.join(settings.MEDIA_ROOT,'generic_profile_image.png'),
    )

    def __unicode__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=60)
    eventimg = models.ImageField(
        upload_to='images/evento/',
        default=os.path.join(settings.MEDIA_ROOT, 'generic_profile_image.png'),
    )

    def __unicode__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=60, verbose_name='Nombre')
    etype = models.ForeignKey('EventType', default=1, related_name='templates', verbose_name='Tipo de evento', )
    teqtype = models.ForeignKey('TequilaType', default=3, verbose_name='Tipo de tequila',)
    timage = models.ImageField(
        verbose_name='Plantilla',
        upload_to='images/templates/',
        default=os.path.join(settings.STATIC_ROOT, 'generic_profile_image.png'),
    )


    #def save(self, *args, **kwargs):
    #    super(Template, self).save(*args, **kwargs)
    #    if self.timage:
    #        fileimage = str(self.timage.path)
    #        img = Image.open(fileimage)
    #        newW = 323
    #        newH = 323 * self.timage.height/self.timage.width
    #        img = img.resize((newW, newH), Image.ANTIALIAS)
    #        img.save(fileimage)





    def __unicode__(self):
        return self.name


class BoxPresentation(models.Model):
    bottlesize = models.CharField(max_length=20)
    bottles = models.PositiveSmallIntegerField()
    maxlabels = models.PositiveSmallIntegerField()
    bottlerow = models.PositiveSmallIntegerField()
    img_original_size = models.ImageField(
        upload_to='images/boxpresentation/',
        default=os.path.join(settings.STATIC_ROOT, 'generic_profile_image.png'),
    )
    img_zoom_size = models.ImageField(
        upload_to='images/boxpresentation/',
        default=os.path.join(settings.STATIC_ROOT, 'generic_profile_image.png'),
    )
    img_tag = models.ImageField(
        upload_to='images/boxpresentation/',
        default=os.path.join(settings.STATIC_ROOT, 'generic_profile_image.png'),
    )
    type = models.ForeignKey('TequilaType', default=1, related_name='sizes')

    def __unicode__(self):
        return self.bottlesize

#from PIL import Image
class CustomImage(models.Model):
    file = models.ImageField(
        upload_to='images/custom/',
        default=os.path.join(settings.STATIC_ROOT, 'generic_profile_image.png')
    )
    name = models.CharField(max_length=30, blank=True, null=True)

    #def save(self):

        #if not self.file:
        #    return

    #    super(CustomImage, self).save()

    #    image = Image.open(self.file)
    #    (width, height) = image.size

    #    print 'width:'
    #    print width
    #    print 'height:'
    #    print height
        #"Max width and height 800"
        #if (800 / width < 800 / height):
        #    factor = 800 / height
        #else:
        #    factor = 800 / width

        #size = ( width / factor, height / factor)
        #image.resize(size, Image.ANTIALIAS)
        #image.save(self.file.path)