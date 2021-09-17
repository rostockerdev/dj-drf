from django.urls import path

from api.views.classbas_api import ArticleDetailApiView, ArticleListApiView
from api.views.funbased_api import art_detail_fun_api, art_list_fun_api
from api.views.regular_views import article_detail, article_list

app_name = "api"

urlpatterns = [
    path("", article_list, name="article-list"),
    path("<pk>/", article_detail, name="article-detail"),
    path("fun_api/", art_list_fun_api, name="fun-article-list"),
    path(
        "fun_api/<pk>/",
        art_detail_fun_api,
        name="fun-article-detail",
    ),
    path(
        "class_api/",
        ArticleListApiView.as_view(),
        name="class-article-list",
    ),
    path(
        "class_api/<pk>/",
        ArticleDetailApiView.as_view(),
        name="class-article-detail",
    ),
]
