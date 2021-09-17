from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from api.models import Article
from api.serializers import ArticleSerializer


class GenViewsetArticleApi(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
