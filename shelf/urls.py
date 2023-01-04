from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_items, name='items'),
    path('folder/', views.get_folder, name='folder'),
    path('add_item', views.add_item, name='add_item'),
    path('add_folder', views.add_folder, name='add_folder'),
]
