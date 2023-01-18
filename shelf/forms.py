from django import forms
from django.forms import TextInput
from .models import Item, Category


class ItemForm(forms.ModelForm):
    add_item = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Item
        fields = ['name', 'quantity', 'notes']
        widgets = {
            'notes': TextInput(attrs={
                'style': 'height: 2.5em;',
                }),
        }


class CategoryForm(forms.ModelForm):
    add_category = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Category
        fields = ['name']

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if (name == ""):
    #         raise forms.ValidationError('This field cannot be left blank')

    #     for instance in Category.objects.filter(user=request.user):
    #         if instance.name == name:
    #             raise forms.ValidationError('There is a category with the name ' + name)
    #     return name
