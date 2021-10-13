from django import forms
from .models import *

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name', 'email', 'country', 'game','score']
 
    