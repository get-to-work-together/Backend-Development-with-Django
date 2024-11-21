from django.urls import path


from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:id>/', views.book, name='book'),
    path('add_book', views.add_book),
]
