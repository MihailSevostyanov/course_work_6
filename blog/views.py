from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogForm
from blog.models import Blog
from blog.services import get_cached_blog_list


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_list'] = get_cached_blog_list()
        return context

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object

class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    permission_required = "blog.add_blog"
    success_url = reverse_lazy("blog:blog_list")
    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        new_article = form.save()
        new_article.slug = slugify(new_article.title)
        new_article.save()

        get_cached_blog_list(recached=True)
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('blog:blog_list')



class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    permission_required = "blog.change_article"
    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

            get_cached_blog_list(recached=True)
            return super().form_valid(form)
    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.delete_article"
    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        get_cached_blog_list(recached=True)
        return super().form_valid(form)

