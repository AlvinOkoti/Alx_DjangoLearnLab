from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import BookListView

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # include API URLs
    path('books/', BookListView.as_view(), name='book-list'),
]
