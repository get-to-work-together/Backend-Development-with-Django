from django.shortcuts import render
from django.http import HttpResponse


titles = [
    'Harry Potter en de Steen der Wijzen',
    'Harry Potter en de Geheime Kamer',
    'Harry Potter en de Gevangene van Azkaban',
    'Harry Potter en de Vuurbeker',
    'Harry Potter en de Orde van de Feniks',
    'Harry Potter en de Halfbloed Prins',
    'Harry Potter en de Relieken van de Dood',
]


def build_html_table(items):
    html = '<table>'
    html += ''.join(f'<tr><td>{item}</td></tr>' for item in items)
    html += '</table>'
    return html


def books(request):
    q = request.GET.get('q', None)
    if q:
        filtered_titles = [title for title in titles if q.lower() in title.lower()]
        return HttpResponse(build_html_table(filtered_titles))
    else:
        return HttpResponse(build_html_table(titles))


def book_detail(request, id):
    try:
        return HttpResponse(titles[id])
    except:
        return HttpResponse('No book found.')
