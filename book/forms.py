from django import forms

class BookCreateForm(forms.Form):
    book_name=forms.CharField()
    author=forms.CharField()
    pages=forms.IntegerField()
    price=forms.IntegerField()