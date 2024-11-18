from django.urls import path

from .views import books, book_detail


urlpatterns = [
    path('', books, name='books'),
    path('<int:id>/', book_detail, name='book_detail'),
]