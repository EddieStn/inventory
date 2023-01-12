from django import forms
from .models import Item, Category


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'category', 'notes']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
