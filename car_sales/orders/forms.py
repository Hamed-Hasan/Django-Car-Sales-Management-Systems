from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['additional_field1', 'additional_field2']
        # Include any other fields that are relevant to the order
