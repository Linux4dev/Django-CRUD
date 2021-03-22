from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from App.models import Book
from App.forms import BookForm

def homePage(request):
    bookForm = BookForm(request.POST or None)
    books = Book.objects.all()
    context = {'Books': books, 'BookForm': bookForm}

    if bookForm.is_valid():
        bookForm.save()
        return redirect('home')
    else:
        return render(request, 'index.html', context)

def deleteBook(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()

    return redirect('home')

def readBook(request, id):
    book = get_object_or_404(Book, pk=id)
    bookForm = BookForm(request.POST or None, instance=book)
    context = {'Book': book, 'BookForm': bookForm}

    if bookForm.is_valid():
        bookForm.save();
        return redirect('readBook', id=id)
    else:
        return render(request, 'read.html', context)