from django.shortcuts import render, redirect
from books_authors_app.models import Book, Author

def index(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request,'index.html',context)

def book_create(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')

def book_detail(request, book_id):
    context = {
        'book' : Book.objects.get(id=book_id),
        'authors' : Book.objects.get(id=book_id).authors.all(),
        'authors_list' : Author.objects.all(),
    }
    return render(request,'book.html', context)

def book_add_author(request,book_id):
    print(request.POST)
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect('/book/'+str(book_id))

def index2(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request,'index2.html',context)

def author_create(request):
    Author.objects.create(
        fname = request.POST['fname'],
        lname = request.POST['lname'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def author_detail(request, author_id):
    context = {
        'author' : Author.objects.get(id=author_id),
        'books' : Author.objects.get(id=author_id).books.all(),
        'books_list' : Book.objects.all(),
    }
    return render(request,'author.html', context)

def author_add_book(request,author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect('/author/'+str(author_id))