from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import ItemForm, CategoryForm


@login_required
def get_items(request):
    items = Item.objects.all()
    category = Category.objects.all()
    context = {
        'items': items,
        'category': category
    }
    return render(request, 'items.html', context)


@login_required
def get_category(request):
    category = Category.objects.all()
    items = Item.objects.filter(category=category)
    context = {
        'category': category
    }
    return render(request, 'category.html', context)


@login_required
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


def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('items')
    return render(request, 'item_delete.html')


def item_edit(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'item_edit.html', context)


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'add_category.html', context)


def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    return render(request, 'category_delete.html')


def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
    }
    return render(request, 'category_edit.html', context)