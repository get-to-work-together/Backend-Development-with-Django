from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.CharField(max_length=100)  # Author's name
    publication_date = models.DateField()  # Publication date
    isbn = models.CharField(max_length=13, unique=True)  # ISBN number (typically 13 characters)
    pages = models.PositiveIntegerField()  # Number of pages
    language = models.CharField(max_length=30, default="English")  # Language of the book
    genre = models.CharField(max_length=60, blank=True)  # Genre of the book
    summary = models.TextField(blank=True)  # Short summary of the book (optional)
    
    # String representation of the model
    def __str__(self):
        return self.title
    