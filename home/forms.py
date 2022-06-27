from django import forms
from home.models import FeedBack


class FeedBackForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=100, label="Phone")
    message = forms.CharField(max_length=1000, label="Message")

    def save(self):
        feedback = FeedBack(**self.cleaned_data)
        feedback.save()
