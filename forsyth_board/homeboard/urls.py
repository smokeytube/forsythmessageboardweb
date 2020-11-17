from django.urls import path
from .views import PostListViewHome, PostDetailViewHome, PostCreateViewHome, PostUpdateViewHome, PostDeleteViewHome, UserPostListViewHome
from . import views

urlpatterns = [
    path('', views.home, name='homeboard-home'),
    path('user/<str:username>', UserPostListViewHome.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailViewHome.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateViewHome.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteViewHome.as_view(), name='post-delete'),
    path('post/new/', PostCreateViewHome.as_view(), name='post-create'),
]


