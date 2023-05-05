from django.db import models

# Create your models here.

class Author(models.Model):

    name = models.CharField('Author name', max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    name = models.CharField('Book name', max_length=100)
    img = models.ImageField('Book image', upload_to='book_images')
    price = models.PositiveIntegerField('Book price')
    ganre = models.CharField('Book ganre', max_length=30)
    about = models.TextField('Book about')

    def __str__(self):
        return self.name