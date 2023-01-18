from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,
                             related_name='category', null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    notes = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name
