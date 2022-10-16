# Restricting user to access pages without login
from dataclasses import fields
import BRMAPP
from django.shortcuts import render
from BRMAPP.forms import NewBookForm, SearchBookForm
from BRMAPP import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def userLogin(request):
    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect('BRMAPP/view-books')
        else:
            data['error'] = 'username or password is incorrect'
            res = render(request, 'BRMAPP/user_login.html', data)
            return res
    else:
        res = render(request, 'BRMAPP/user_login.html', data)
        return res


def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRMAPP/login/')
# Book Record Management | View Book Records


@login_required(login_url='/BRMAPP/login/')
def viewBook(request):
    books = models.Book.objects.all()
    username = request.session['username']
    res = render(request, 'BRMAPP/view_book.html',
                 {'books': books, 'username': username})
    return res
# Book Record Management | Search Book Record


@login_required(login_url='/BRMAPP/login/')
def searchBook(request):
    form = SearchBookForm()
    res = render(request, 'BRMAPP/search_book.html', {'form': form})
    return res


@login_required(login_url='/BRMAPP/login/')
def search(request):
    form = SearchBookForm(request.POST)
    books = models.Book.objects.filter(title=form.data['title'])
    res = render(request, 'BRMAPP/search_book.html',
                 {'form': form, 'books': books})
    return res
# Book Record Management|Delete a book


@login_required(login_url='/BRMAPP/login/')
def deleteBook(request):
    bookid = request.GET['bookid']
    book = models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMAPP/view-books')
# Book Record Management | Add New Book Record


@login_required(login_url='/BRMAPP/login/')
def newBook(request):
    form = NewBookForm()
    res = render(request, 'BRMAPP/new_book.html', {'form': form})
    return res


@login_required(login_url='/BRMAPP/login/')
def add(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = models.Book()
        book.title = form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    s = "Record Stored <br><a href='/BRMAPP/view-books'>view all Books</a>"
    return HttpResponse(s)


@login_required(login_url='/BRMAPP/login/')
def edit(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = models.Book()
        book.id = request.POST['bookid']
        book.title = form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    return HttpResponseRedirect('BRMAPP/view-books')


@login_required(login_url='/BRMAPP/login/')
def editBook(request):
    models.Book.objects.filter(id=request.GET['bookid'])
    book = models.Book.objects.get(id=request.GET['bookid'])
    fields = {'title': book.title, 'price': book.price, 'author': book.author,
              'publisher': book.publisher}
    form = NewBookForm(initial=fields)
    res = render(request, 'BRMAPP/edit_book.html',
                 {'form': form, 'book': book})
    return res
