from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleListApiView(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serialize_data = ArticleSerializer(articles, many=True)
        return Response(data=serialize_data.data)

    def post(self, request, format=None):
        serialize_data = ArticleSerializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailApiView(APIView):
    def get_object(self, pk):
        try:
            article = Article.objects.get(id=pk)
            return article
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serialize_data = ArticleSerializer(article)
        return Response(serialize_data.data, status=status.HTTP_302_FOUND)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serialize_data = ArticleSerializer(article, data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
