from django.db import models


class Cover(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to='cover/')
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
