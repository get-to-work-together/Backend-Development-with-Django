from django.urls import path

from .views import books, add_book
from .views import CustomLoginView


urlpatterns = [
    path('', books, name='books'),
    path('add-book/', add_book, name='add_book'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
