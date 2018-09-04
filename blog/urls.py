from django.urls import path

from . import views

urlpatterns = [
    path('artice-list/', views.ArticleListing.as_view(), name='article-listing'),
    path('article-detail/<slug:article_id>/', views.ArticleDetail.as_view(), name='article-detail')
]