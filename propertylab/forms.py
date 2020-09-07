from django import forms
from crispy_forms.helper import FormHelper

class WebsiteEnquiryForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))    
    phone = forms.CharField(label='Phone Number')
    message = forms.CharField(widget=forms.Textarea)