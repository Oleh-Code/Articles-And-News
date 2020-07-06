from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_list'),
    path('post/<slug:slug>/', views.ArticlesDetailView.as_view(), name='articles_detail'),
    path('post/new/', views.form, name='post_new')
]