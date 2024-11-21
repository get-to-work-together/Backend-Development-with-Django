from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm


def books(request):
    q = request.GET.get('q', '')
    fields = ['id', 'title', 'author', 'publication_year', 'isbn']
    books = Book.objects.all()
    if q:
        books = books.filter(title__icontains=q)
    books = books.values(*fields)
    verbose_names = [Book._meta.get_field(field).verbose_name for field in fields]
    context = {'data': books, 'title': 'Boeken', 'verbose_names': verbose_names}
    return render(request, 'books.html', context)

def book(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'data': book, 'title': 'Een Boek'}
    return render(request, 'book.html', context)


def add_book(request):
    form = BookForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('/books')
        else:
            form = BookForm()

    return render(request, 'add_book.html', {'form': form})
