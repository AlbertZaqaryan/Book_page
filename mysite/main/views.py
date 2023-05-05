from django.shortcuts import render
from .models import Book
# Create your views here.


def home(request):
    book_list = Book.objects.all()
    return render(request, 'main/home.html', context={
        'book_list':book_list
    })


def home_detail(request, id):
    one_book = Book.objects.get(pk=id)
    return render(request, 'main/home_detail.html', context={
        'one_book':one_book
    })