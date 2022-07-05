from django import forms

from marketplace.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'image', 'price',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
