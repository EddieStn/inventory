from django import forms
from .models import Item, Category


class ItemForm(forms.ModelForm):
    add_item = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Item
        fields = ['name', 'quantity', 'category', 'notes']


class CategoryForm(forms.ModelForm):
    add_category = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Category
        fields = ['name']
