# Generated by Django 5.1.3 on 2024-11-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_publication_date_book_publication_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='year'),
        ),
    ]
