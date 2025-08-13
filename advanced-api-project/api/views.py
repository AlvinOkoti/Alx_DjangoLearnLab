from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from django.urls import reverse
from rest_framework import status
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
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

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

        # Create sample books
        self.book1 = Book.objects.create(title="Django Basics", author="John Doe", price=10)
        self.book2 = Book.objects.create(title="Advanced Django", author="Jane Doe", price=20)

        # Endpoints
        self.list_url = reverse('book-list')  # Adjust based on your router name
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])

    # --- CREATE ---
    def test_create_book(self):
        data = {"title": "New Book", "author": "Mark Smith", "price": 15}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    # --- READ ---
    def test_list_books(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # --- UPDATE ---
    def test_update_book(self):
        data = {"title": "Updated Title", "author": "John Doe", "price": 12}
        response = self.client.put(self.detail_url(self.book1.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # --- DELETE ---
    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    # --- FILTERING ---
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + '?author=Jane Doe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == "Jane Doe" for book in response.data))

    # --- SEARCHING ---
    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Django')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # --- ORDERING ---
    def test_order_books_by_price(self):
        response = self.client.get(self.list_url + '?ordering=price')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        prices = [book["price"] for book in response.data]
        self.assertEqual(prices, sorted(prices))

    # --- PERMISSIONS ---
    def test_unauthenticated_user_cannot_create_book(self):
        self.client.logout()
        data = {"title": "Unauthorized Book", "author": "Someone", "price": 5}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)