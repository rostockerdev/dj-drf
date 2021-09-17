from rest_framework import generics, mixins, status
from rest_framework.response import Response

from api.models import Article
from api.serializers import ArticleSerializer


class ArtilceListGenericApi(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = "pk"

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request, pk)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
