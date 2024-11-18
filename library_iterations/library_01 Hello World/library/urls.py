from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def hello_world(request):
    # Get the 'name' from the query string, default to 'World' if not provided
    name = request.GET.get('name', 'World')

    return HttpResponse(f'Hello, {name}!')


# URL configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world, name='hello_world'),
]
