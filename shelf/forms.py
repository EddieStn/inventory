from django import forms
from .models import Item, Folder


class ItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'folder']


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
