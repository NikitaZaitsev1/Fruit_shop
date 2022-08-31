from django import forms
from home.models import FeedBack

from phonenumber_field.formfields import PhoneNumberField


class FeedBackForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = FeedBack
        fields = ('full_name', 'email', 'phone', 'message')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
