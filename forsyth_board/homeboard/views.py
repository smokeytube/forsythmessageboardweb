from .models import Posthome
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Posthome.objects.all()
    }
    return render(request, 'homeboard/homeboard.html', context)



class PostListViewHome(ListView):
    model = Posthome
    template_name = 'brandom/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class UserPostListViewHome(ListView):
    model = Posthome
    template_name = 'brandom/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posthome.objects.filter(author=user).order_by('-date_posted')

class PostDetailViewHome(DetailView):
    model = Posthome


class PostCreateViewHome(LoginRequiredMixin, CreateView):
    model = Posthome
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateViewHome(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posthome
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteViewHome(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posthome
    success_url = '/brandom/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


        

    