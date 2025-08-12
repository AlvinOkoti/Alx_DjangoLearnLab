from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import BookSerializer
from django_filters import rest_framework as django_filters

# 1. ListView - GET all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read

# 2. DetailView - GET a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read

# 3. CreateView - POST new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# 4. UpdateView - PUT/PATCH existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# 5. DeleteView - DELETE a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books.
    Supports:
    - Filtering by title, author, and publication_year
    - Searching by title or author's name
    - Ordering by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filter, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filterable fields (by exact match)
    filterset_fields = ['title', 'author', 'publication_year']

    # Searchable fields (partial match)
    search_fields = ['title', 'author__name']

    # Orderable fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']