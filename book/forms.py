from django import forms
from django.forms import  ModelForm
from .models import Book
#class BookCreateForm(forms.Form):
#   book_name=forms.CharField()
#    author=forms.CharField()
#    pages=forms.IntegerField()
#    price=forms.IntegerField()


#django Modelform

class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields=["book_name","author","price","pages"]
    def clean(self):
        print("validation here")