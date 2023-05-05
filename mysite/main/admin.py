from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ganre']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price', 'ganre']
