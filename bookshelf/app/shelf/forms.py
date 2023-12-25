#from django.core.exceptions import ValidationError
from django.forms import ModelForm, ValidationError 
from django import forms
from .models import Book
import isbnlib

class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["isbn", "bookfile"]

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.fields['isbn'].widget.attrs.update({'class': 'form-control', 'autofocus': True, 'aria-label' : 'Large', 'aria-describedby' : 'inputGroup-sizing-sm'})
        self.fields['bookfile'].widget.attrs.update({'class': 'form-control', 'aria-label' : 'Large', 'aria-describedby' : 'inputGroup-sizing-sm'})
