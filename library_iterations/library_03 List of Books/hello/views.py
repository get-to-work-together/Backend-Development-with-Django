from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    # Get the 'name' from the query string, default to 'World' if not provided
    name = request.GET.get('name', 'World')

    return HttpResponse(f'Hello, {name}!')
