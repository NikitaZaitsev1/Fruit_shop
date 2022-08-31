from django import forms
from phonenumber_field.formfields import PhoneNumberField

from order.models import Order


class OrderForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ('product', 'address', 'phone', 'quantity')
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'})
        }
