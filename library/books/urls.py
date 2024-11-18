from django.urls import path

from .views import books, add_book
from .views import CustomLoginView
from .views import BookList, BookDetail


urlpatterns = [
    path('', books, name='books'),
    path('add-book/', add_book, name='add_book'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('api/books/', BookList.as_view(), name='book_list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]

