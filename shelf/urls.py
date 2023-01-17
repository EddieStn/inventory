from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:pk>', views.item_delete, name='item-delete'),
    path('edit/<int:pk>', views.item_edit, name='item-edit'),
    path('delete_category/<int:pk>', views.category_delete,
         name='category-delete'),
    path('edit_category/<int:pk>', views.category_edit,
         name='category-edit'),
]
