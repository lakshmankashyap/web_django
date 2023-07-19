from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is the books homepage</h1>")


def detail(request, book_id):
    return HttpResponse(f"<h2>Details for Book ID: {book_id}</h2>")
