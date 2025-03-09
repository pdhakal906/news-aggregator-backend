from django.urls import path
from .views import ListNews, TestView


urlpatterns = [
    path("", ListNews.as_view()),
    path("test", TestView.as_view()),
]
