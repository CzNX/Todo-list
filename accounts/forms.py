from .models import Todo
from django import forms


class MyForm(forms.ModelForm):

  class Meta:
    model = Todo
    fields ='__all__'