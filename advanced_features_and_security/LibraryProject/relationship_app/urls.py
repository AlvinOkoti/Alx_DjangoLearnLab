# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),  # Optional home view after login
    
    # Books redirection
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
     path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Other URLs
    path('books/', views.list_books, name='list_books'),  # for redirection after login
]
# Defining URL views and patterns
urlpatterns = [
    path('admin-panel/', views.admin_view, name='admin_view'),
    path('librarian-panel/', views.librarian_view, name='librarian_view'),
    path('member-panel/', views.member_view, name='member_view'),

    # Existing URLs
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', views.home, name='home'),
    
     # Book permission-controlled URLs
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Other URLs (if not already present)
    path('admin-panel/', views.admin_view, name='admin_view'),
    path('librarian-panel/', views.librarian_view, name='librarian_view'),
    path('member-panel/', views.member_view, name='member_view'),

    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', views.home, name='home'),
]

