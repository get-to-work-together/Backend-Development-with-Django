from django.urls import path

from .views import books, book_detail
from .views import CustomLoginView


urlpatterns = [
    path('', books, name='books'),
    path('<int:id>/', book_detail, name='book_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
