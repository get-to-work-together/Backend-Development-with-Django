from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True) 

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')  # Title of the book
    author = models.CharField(max_length=100, blank=True, null=True, verbose_name='Author')  # Author's name
    publication_year = models.IntegerField(blank=True, null=True, verbose_name='Year')  # Publication year
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True, verbose_name='ISBN')  # ISBN number (typically 13 characters)
    pages = models.PositiveIntegerField(blank=True, null=True, verbose_name='Pages')  # Number of pages
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Genre')  # Genre
    language = models.CharField(max_length=30, default="English", blank=True, null=True, verbose_name='Language')  # Language of the book
    summary = models.TextField(blank=True, null=True, verbose_name='Sumamry')  # Short summary of the book (optional)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Price')  # Price of the book
    
    # String representation of the model
    def __str__(self):
        return self.title
    
    

