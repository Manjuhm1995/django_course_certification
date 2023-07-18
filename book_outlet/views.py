from django.shortcuts import render,get_object_or_404
from django.http import Http404
from . models import Book

# Create your views here.

def index(request):
    books=Book.objects.all()
    return render(request,"book_outlet/index.html",{"books":books})

def book_detail(request,slug):
    # try:
    #     books=Book.objects.get(id=id)
    # except:
    #     raise Http404()
    books=get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        "title":books.title,
        "author":books.author,
        "is_bestseller":books.is_bestselling,
        "rating":books.rating})