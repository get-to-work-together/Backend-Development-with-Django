from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.CharField(max_length=100)  # Author's name
    publication_date = models.DateField()  # Publication date
    isbn = models.CharField(max_length=13, unique=True)  # ISBN number (typically 13 characters)
    pages = models.PositiveIntegerField()  # Number of pages
    # cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # Cover image (optional)
    language = models.CharField(max_length=30, default="English")  # Language of the book
    summary = models.TextField(blank=True)  # Short summary of the book (optional)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the book
    
    # String representation of the model
    def __str__(self):
        return self.title
