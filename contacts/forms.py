from django import forms
from django.forms import ModelForm
from contacts.models import Contact
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('date_created', 'created_by')