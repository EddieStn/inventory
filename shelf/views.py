from django.shortcuts import render
from django.views import generic
from .models import Item, Folder


class ItemList(generic.ListView):
    model = Item
    queryset = Item.objects.order_by('-timestamp')
    template_name = 'index.html'
    paginate_by = 10


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        quantity = request.POST.get(Item.quantity)
        folder = request.POST.get(Item.folder)
        Item.objects.create(name=name, quantity=quantity, folder=folder)

        return redirect('index.html')
    return render(request, 'add_item.html')


class FolderList(generic.ListView):
    model = Folder
    template_name = 'index.html'
