from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import Article
from .forms import ArticleForm

class ArticlesListView(ListView):
    model = Article
    queryset = Article.objects.filter(draft=False).order_by('published_date')

class ArticlesDetailView(DetailView):
    model = Article
    queryset = Article.objects.filter(draft=False)
    slug_field = 'url'

def form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('articles_detail', slug=post.url)
    else:
        form = ArticleForm()

        return render(request, 'Site/new_article.html', locals())
