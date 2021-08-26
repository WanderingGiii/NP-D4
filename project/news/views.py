from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from datetime import datetime
from .filters import PostFilter

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-datetime']
    paginate_by = 5
    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-datetime']
    paginate_by = 5
    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class NewsView(DetailView):
    model = Post, Comment
    template_name = 'newsdetail.html'
    context_object_name = 'newsdetail'
    ordering = ['-id']
    paginate_by = 1
    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class CommentList(ListView):
    model = Post, Comment
    template_name = 'newsdetail.html'
    context_object_name = 'comments'
    queryset = Comment.objects.order_by('-id')

class CommentView(DetailView):
    model = Post, Comment
    template_name = 'newsdetail.html'
    context_object_name = 'comment'
    queryset = Post.objects.order_by('-id')




