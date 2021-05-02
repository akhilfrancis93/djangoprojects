from django.shortcuts import render,redirect
from.forms import BookCreateForm
from.models import Book
# Create your views here.


def create_book(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data.get("book_name")
            author=form.cleaned_data.get("author")
            pages=form.cleaned_data.get("pages")
            price=form.cleaned_data.get("price")
            book=Book(book_name=book_name,author=author,pages=pages,price=price)
            book.save()
            print("saved")
            return redirect("list")
        else:
            pass

    return render(request,"book/createbook.html",context)


def list_all_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"book/listallbooks.html",context)

def book_detail(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookdetail.html",context)


def book_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("list")

def book_update(request,id):
    book=Book.objects.filter(id=id)
