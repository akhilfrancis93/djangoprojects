from django.shortcuts import render,redirect
from.forms import BookCreateForm
from.models import Book
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def create_book(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
       form=BookCreateForm(request.POST)
    if form.is_valid():
        form.save()
#            book_name=form.cleaned_data.get("book_name")
#            author=form.cleaned_data.get("author")
#           pages=form.cleaned_data.get("pages")
#            price=form.cleaned_data.get("price")
#            book=Book(book_name=book_name,author=author,pages=pages,price=price)
#            book.save()
#            print("saved")
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
    book=Book.objects.get(id=id)
    form=BookCreateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("list")

    return render(request,"book/editbook.html",context)

def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
            return render(request, "book/registration.html", context)
    return render(request,"book/registration.html",context)

def login_user(request):
    context={}
    form=LoginForm()
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"book/index.html")
    return render(request,"book/login.html",context)


def signout(request):
    logout(request)
    return redirect("userlogin")
