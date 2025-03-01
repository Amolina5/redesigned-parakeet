from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
)

from .models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = [
        'title', 'subtitle', 'body', 'status',
    ]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('list')  # Ensure 'list' is a valid URL pattern

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts_list'  # Consistent naming

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published = Status.objects.get(name='published')
        context["posts_list"] = (  # Consistent naming
            Post.objects
            .filter(status=published)
            .order_by("created_on").reverse()
        )
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name='draft')
        context["posts_list"] = (  # Consistent naming
            Post.objects
            .filter(status=draft)
            .filter(author=self.request.user)
            .order_by("created_on").reverse()
        )
        return context

class ArchivePostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archive = Status.objects.get(name='archived')  # Corrected retrieval
        context["posts_list"] = (  # Consistent naming
            Post.objects
            .filter(status=archive)
            .order_by("created_on").reverse()
        )
        return context

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = [
        'title', 'subtitle', 'body', 'status',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
