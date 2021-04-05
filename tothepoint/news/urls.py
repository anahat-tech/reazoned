from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('index/', views.index, name='index'),
   path('index/article/', views.article_detail, name='article_detail'),
   path('article/', views.article_detail, name='article_detail'),
   path('world/', views.world, name='world'),
   path('world/article/', views.article_detail, name='article_detail'),
   path('business/', views.business, name='business'),
   path('business/article/', views.article_detail, name='article_detail'),
   path('tech/', views.tech, name='tech'),
   path('tech/article/', views.article_detail, name='article_detail'),
   path('sports/', views.sports, name='sports'),
   path('sports/article/', views.article_detail, name='article_detail'),
   path('entertainment/', views.entertainment, name='entertainment'),
   path('entertainment/article/', views.article_detail, name='article_detail'),
   path('opinion/', views.opinion, name='opinion'),
   path('opinion/article/', views.article_detail, name='article_detail'),
]