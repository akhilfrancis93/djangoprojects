4
"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from.views import create_book,list_all_book,book_detail,book_delete,book_update,registration,login_user,signout

urlpatterns = [
    path("create",create_book,name="createbook"),
    path("list",list_all_book,name="list"),
    path("detail/<int:id>",book_detail,name="detail"),
    path("delete/<int:id>",book_delete,name="delete"),
    path("edit/<int:id>",book_update,name="edit"),
    path("registeration",registration,name="register"),
    path("login",login_user,name="userlogin"),
    path("logout",signout,name="signout")
]
