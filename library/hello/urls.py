from django.urls import path

from .views import hello_world, hello_again


urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('html/', hello_again, name='hello_again'),
]