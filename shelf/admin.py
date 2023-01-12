from django.contrib import admin
from .models import Item, Category

admin.site.site_header = 'Inventory'


class ItemAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'name', 'category', 'notes', )
    list_filter = ('category', 'created_on')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
