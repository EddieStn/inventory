from django.db import models
from cloudinary.models import CloudinaryField


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    crated_on = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name
