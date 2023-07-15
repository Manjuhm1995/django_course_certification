from django.shortcuts import render
from . models import Book

# Create your views here.

def index(request):
    books=Book.objects.all()
    return render(request,"book_outlet/index.html",{"books":books})

def book_detail(request,id):
    books=Book.objects.get(id=id)
    return render(request,"book_outlet/book_detail.html",{
        "title":books.title,
        "author":books.author,
        "is_bestseller":books.is_bestselling,
        "rating":books.rating})