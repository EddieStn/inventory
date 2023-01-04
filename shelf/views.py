from django.shortcuts import render, redirect
from django.views import generic
from .models import Item, Folder
from .forms import ItemForm, FolderForm


def get_items(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'items.html', context)


def get_folder(request):
    folder = Folder.objects.all()
    context = {
        'folder': folder
    }
    return render(request, 'folder.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'add_item.html', context)


def add_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('folder')
    form = FolderForm()
    context = {
        'form': form
    }
    return render(request, 'add_folder.html', context)
