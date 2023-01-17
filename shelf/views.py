from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from .models import Item, Category
from .forms import ItemForm, CategoryForm


@login_required
def index(request):

    items = Item.objects.all()
    category = Category.objects.all()
    add_item = ItemForm()
    add_category = CategoryForm()
    query = None
    categories = None

    if request.method == 'POST':
        if 'add_item' in request.POST:
            add_item = ItemForm(request.POST)
            if add_item.is_valid():
                add_item.save()
        if 'add_category' in request.POST:
            add_category = CategoryForm(request.POST)
            if add_category.is_valid():
                add_category.save()

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            items = items.filter(category__name__in=category)
            categories = Category.objects.filter(name__in=category)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(notes__icontains=query)
            items = items.filter(queries)

    context = {
        'items': items,
        'search_term': query,
        'current_categories': categories,
        'category': category,
        'add_item': add_item,
        'add_category': add_category,
    }
    return render(request, 'index.html', context)


@login_required
def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'item_delete.html')


@login_required
def item_edit(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'item_edit.html', context)


@login_required
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('home')
    return render(request, 'category_delete.html')


@login_required
def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
    }
    return render(request, 'category_edit.html', context)
