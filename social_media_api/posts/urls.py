from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="post")
router.register(r'comments', CommentViewSet, basename="comment")

urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # auth routes
    path('api/', include('posts.urls')),  # posts and comments route
]
