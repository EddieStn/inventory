from django.shortcuts import render
from django.views import generic
from .models import Item


class ItemList(generic.ListView):
    model = Item
    queryset = Item.objects.order_by('-timestamp')
    template_name = 'index.html'
    paginate_by = 10
