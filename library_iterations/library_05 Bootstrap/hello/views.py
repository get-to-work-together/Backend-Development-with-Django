from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    # Get the 'name' from the query string, default to 'World' if not provided
    name = request.GET.get('name', 'World')

    return HttpResponse(f'Hello, {name}!')


# View that uses a template
def hello_again(request):
    context = {
        'name': request.GET.get('name', 'World')  # Pass 'name' to the template
    }
    return render(request, 'hello.html', context)  # Render the 'hello.html' template
