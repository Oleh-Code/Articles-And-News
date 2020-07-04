from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticlesListView(ListView):
    model = Article
    queryset = Article.objects.filter(draft=False).order_by('published_date')

class ArticlesDetailView(DetailView):
    model = Article
    queryset = Article.objects.filter(draft=False)
    slug_field = 'url'