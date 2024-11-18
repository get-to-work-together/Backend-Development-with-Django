from django import forms
from .models import *
from django.forms.widgets import DateTimeInput

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['code', 
                  'name']
