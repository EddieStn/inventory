from django import forms
from django.contrib.auth.models import User
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

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if (name == ""):
            raise forms.ValidationError('This field cannot be left blank')
        qs = Category.objects.filter(user=self.user, name=name)
        if self.instance.pk:
            # EXCLUDE CURRENT INSTANCE TO ENABLE EDIT
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('There is a category with the name ' + name)
        return name
