from django.forms import ModelForm, fields
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price']