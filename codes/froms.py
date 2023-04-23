from dataclasses import field
from django import forms
from .models import Code

class CodeForm(forms.Form):
    number = forms.CharField(label='code', help_text='Enter SMS verification')
    class meta:
        model = Code
        fields = ('number')
        