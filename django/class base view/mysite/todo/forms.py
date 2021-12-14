from django import forms
from .models import Todo

class Todo_form(forms.Form):
    title = forms.CharField(max_length=200)