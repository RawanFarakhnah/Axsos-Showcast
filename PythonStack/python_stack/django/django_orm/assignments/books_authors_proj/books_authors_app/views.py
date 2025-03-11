from django.shortcuts import render, redirect, HttpResponse
from .models import Author, Book

# Create your views here.
def root(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "root.html", context)

def create_book(request):
    if request.method == "POST":
      title=request.POST.get('title', '')
      desc=request.POST.get('desc', '')
      Book.objects.create(title=title, desc=desc);
      return redirect('root')
    
    return redirect('root')

def view_book(request, id):
    book_id = int(id)
    this_book = Book.objects.get(id=book_id)
    all_authors = Author.objects.exclude(books__id=book_id)
   
    context = {
       'book': this_book,
       'all_authors': all_authors
    }
    return render(request, 'view_book.html', context)

def update_book_authors(request):
    if request.method == "POST":
       book_id = int(request.POST.get('book_id', '0'))
       author_id = int(request.POST.get('author_id', '0'))
        
       if int(book_id) > 0 and int(author_id) > 0:
         this_book = Book.objects.get(id=int(book_id))
         this_author = Author.objects.get(id=int(author_id))
         this_book.authors.add(this_author)
         return redirect('view_book', id=int(book_id))
       
       return redirect('view_book', id=int(book_id))
         

def author(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, "author.html", context)

def create_author(request):
    if request.method == "POST":
      last_name=request.POST.get('last_name', '')
      first_name=request.POST.get('first_name', '')
      notes=request.POST.get('notes','')
      Author.objects.create(first_name=first_name, last_name=last_name, notes=notes);
      return redirect('author')
    
    return redirect('author')

def view_author(request, id):
    author_id = int(id)
    this_author = Author.objects.get(id=author_id)
    all_books = Book.objects.exclude(authors__id=author_id)
   
    context = {
       'author': this_author,
       'all_books': all_books
    }
    return render(request, 'view_author.html', context)

def update_author_books(request):
    if request.method == "POST":
       book_id = request.POST.get('book_id', 0)
       author_id = request.POST.get('author_id', 0)

       if  int(book_id) > 0 and int(author_id) > 0:
         this_book = Book.objects.get(id=int(book_id))
         this_author = Author.objects.get(id=int(author_id))
         this_author.books.add(this_book)
         return redirect('view_author', id=int(author_id))
       
       return redirect('view_author', id=int(author_id))