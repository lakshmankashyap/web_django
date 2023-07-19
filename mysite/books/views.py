from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    all_books = Book.objects.all()
    html= ''
    for book in all_books:
        url = '/books/'+str(book.id)+'/'
        html+='<a href="'+url+'">'+str(book.name)+'</a><br> '
    return HttpResponse(html)


def detail(request, book_id):
    return HttpResponse(f"<h2>Details for Book ID: {book_id}</h2>")
