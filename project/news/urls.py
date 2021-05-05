from django.urls import path
from .views import NewsList, NewsView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsView.as_view()),
]