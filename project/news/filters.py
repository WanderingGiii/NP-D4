from django_filters import FilterSet, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Author


# создаём фильтр
class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'datetime': ['gt'],
        }
