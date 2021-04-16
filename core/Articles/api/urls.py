from django.contrib import admin
from django.urls import path,include

from Articles.api.views import AuthorViewSet,ArticleViewSet,AvatarUpdateView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'author-list',AuthorViewSet)
router.register(r'article', ArticleViewSet, basename='article')

urlpatterns = [
    path('',include(router.urls )),
    path('avatar/', AvatarUpdateView.as_view(), name='foto'),
]