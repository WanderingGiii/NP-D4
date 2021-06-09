from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from datetime import datetime


class NewsList(ListView):
    model = Post, Comment
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class NewsView(DetailView):
    model = Post, Comment
    template_name = 'newsdetail.html'
    context_object_name = 'newsdetail'
    queryset = Post.objects.order_by('-id')

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




