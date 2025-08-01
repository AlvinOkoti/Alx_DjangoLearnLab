from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title" , "author" , "publication_year")
    list_filter = ("author" , "publication_year")
    search_fields = ("author" , "publication_year")
    