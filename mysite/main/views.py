from django.shortcuts import render
from .models import Book, Author
# Create your views here.


def home(request):
    authors = Author.objects.all()
    return render(request, 'main/home.html', context={
        'authors':authors
    })

def book(request, id):
    book_list = Author.objects.filter(pk=id)
    return render(request, 'main/book.html', context={
        'book_list':book_list
    })

def home_detail(request, id):
    one_book = Book.objects.get(pk=id)
    return render(request, 'main/home_detail.html', context={
        'one_book':one_book
    })