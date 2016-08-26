from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse("category_product_list", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category)
    sku = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images', blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(295, 300)],
                                     format='JPEG',
                                     options={'quality': 60})
    image_thumbnail_xs = ImageSpecField(source='image',
                                        processors=[ResizeToFill(150, 150)],
                                        format='JPEG',
                                        options={'quality': 60})
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse("product_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
