from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Book


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Path to the template we will create


def build_html_table(items):
    html = '<table>'
    html += ''.join(f'<tr><td>{item}</td></tr>' for item in items)
    html += '</table>'
    return html


# def books(request):
#     q = request.GET.get('q', None)
#     if q:
#         q = q.lower()
#         filtered_titles = [title for title in titles if q in title.lower()]
#         return HttpResponse(build_html_table(filtered_titles))
#     else:
#         return HttpResponse(build_html_table(titles))


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


def book_detail(request, id):
    try:
        return HttpResponse(titles[id])
    except:
        return HttpResponse('No book found.')
