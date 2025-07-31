from relationship_app.models import Book, Author

author_name="George Orwell"

author_name = "George Orwell"

try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)

    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'")