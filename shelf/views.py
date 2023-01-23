from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from .models import Item, Category
from .forms import ItemForm, CategoryForm


@login_required
def index(request):

    categories = Category.objects.filter(user=request.user)
    items = Item.objects.filter(user=request.user)
    add_item = ItemForm()
    add_category = CategoryForm(user=request.user)
    query = None

    if request.method == 'POST':
        if 'add_item' in request.POST:
            add_item = ItemForm(request.POST)
            if add_item.is_valid():
                form = add_item.save(commit=False)
                form.category = get_object_or_404(
                    Category, name=request.POST.get('category'),
                    user=request.user)
                add_item.save()
                name = add_item.cleaned_data.get('name')
                messages.success(request, f'{name} has been added')
                return redirect('home')
        else:
            add_category = CategoryForm(user=request.user, data=request.POST)
            if add_category.is_valid():
                category_form = add_category.save(commit=False)
                category_form.user = request.user
                category_form.save()
                name = add_category.cleaned_data.get('name')
                messages.success(request, f'{name} has been added')
                return redirect('home')

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('home'))
            queries = Q(name__icontains=query) | Q(notes__icontains=query)
            items = items.filter(queries)
        if 'category' in request.GET:
            category = get_object_or_404(
                Category, name=request.GET.get('category'), user=request.user)
            items = Item.objects.filter(category=category)

    context = {
        'items': items,
        'search_term': query,
        'add_item': add_item,
        'add_category': add_category,
        'categories': categories
    }
    return render(request, 'index.html', context)


@login_required
def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.error(request, f'{item.name} has been deleted!')
        return redirect('home')
    return render(request, 'item_delete.html')


@login_required
def item_edit(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, f'{item.name} has been updated!')
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
        messages.error(request, f'{category.name} has been deleted!')
        return redirect('home')
    return render(request, 'category_delete.html')


@login_required
def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(user=request.user, data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.info(request, f'{category.name} has been updated!')
            return redirect('home')
        else:
            print('form invalid')
    else:
        form = CategoryForm(instance=category, user=request.user)

    context = {
        'form': form,
    }
    return render(request, 'category_edit.html', context)
