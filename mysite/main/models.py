from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField('Book name', max_length=100)
    img = models.ImageField('Book image', upload_to='book_images')
    price = models.PositiveIntegerField('Book price')
    ganre = models.CharField('Book ganre', max_length=30)
    about = models.TextField('Book about')

    def __str__(self):
        return self.name