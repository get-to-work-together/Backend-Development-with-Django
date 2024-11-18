from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import BookForm


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Path to the template we will create


@login_required
def books(request):
    q = request.GET.get('q', None)
    books = Book.objects.all()
    if q:
        q = q.lower()
        filtered_titles = [book.title for book in books if q.lower() in book.title.lower()]
    else:
        filtered_titles = books
    context = {
        'items': filtered_titles
    }
    return render(request, 'books/list.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book to the database
            return redirect('books')  # Redirect to some other page (e.g., book list)
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})
