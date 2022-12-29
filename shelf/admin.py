from django.contrib import admin
from .models import Item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
    list_display = ('name', 'timestamp')
    search_fields = ['name', 'description']
