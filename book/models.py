from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=150,unique=True)
    author=models.CharField(max_length=120)
    price=models.IntegerField()
    pages=models.IntegerField()

    def __str__(self):
        return self.book_name


    #ORM Queries

#book=Book(book_name="randamoozham",author="mt",price=250,pages=200)
#book.save()
#books=Book.objects.all()
#books
#book=Book.objects.get(id=1)
#print(book.book_name)
#print(book.price)
#for book in books:
#print(book.book_name)
#print(book.price)
#books=Book.objects.filter(price__gte=190) price greater than
#books=Book.objects.filter(price__lte=190) price less than
#book=Book.objects.get(id=1)
# book.delete() delete