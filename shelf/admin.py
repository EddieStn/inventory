from django.contrib import admin
from .models import Item, Folder


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'description', 'folder', )


class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Item, ItemAdmin)
admin.site.register(Folder, FolderAdmin)
