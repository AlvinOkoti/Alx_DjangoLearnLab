from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)

#admin class created
class BookAdmin(admin.ModelAdmin):
    list_display = ("title" , "author" , "publication_year")
    list_filter = ("title" , "publication_year")
    search_fields = ("title" , "author")
    