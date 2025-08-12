from django.db import models

# Author model: Represents a book author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's full name

    def __str__(self):
        return self.name

# Book model: Represents books linked to an author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # related_name='books' allows reverse lookup: author.books.all()

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
