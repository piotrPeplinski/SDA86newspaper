from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListCreate.as_view(), name='articles'),
    path('articles/<int:article_id>/',
         views.ArticleDetail.as_view(), name='detail'),
    path('users/', views.UsersListCreate.as_view(), name='users')
]
