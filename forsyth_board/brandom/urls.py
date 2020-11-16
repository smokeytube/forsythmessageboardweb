#from forsyth_board.brandom.models import Post
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
#from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='brandom-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]