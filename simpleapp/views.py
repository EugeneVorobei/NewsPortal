from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 10

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 10

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class PostDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        categories = []
        post = Post.objects.get(pk=id)
        for cat in post.category.all():
            if self.request.user in cat.subscribers.all():
                categories.append(cat)
        context['user_category'] = categories
        return context


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post',)
    template_name = 'news_add.html'
    form_class = PostForm


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_post',)
    template_name = 'news_add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_post',)
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


@login_required
def subscribe(request, **kwargs):
    user = request.user
    cat_id = kwargs['pk']
    category = Category.objects.get(pk=int(cat_id))

    if user not in category.subscribers.all():
        category.subscribers.add(user)

    else:
        category.subscribers.remove(user)

    return redirect(request.META.get('HTTP_REFERER', '/'))
