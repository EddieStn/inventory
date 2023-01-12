from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_items, name='items'),
    path('category/', views.get_category, name='category'),
    path('add_item', views.add_item, name='add-item'),
    path('delete/<int:pk>', views.item_delete, name='item-delete'),
    path('edit/<int:pk>', views.item_edit, name='item-edit'),
    path('add_category/', views.add_category, name='add-category'),
    path('delete_category/<int:pk>', views.category_delete, name='category-delete'),
    path('edit_category/<int:pk>', views.category_edit, name='category-edit'),
]
