from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_items, name='items'),
    path('category/', views.get_category, name='category'),
    path('add_item', views.add_item, name='add-item'),
    path('delete/<int:pk>', views.item_delete, name='item-delete'),
    path('add_category/', views.add_category, name='add-category'),
]
