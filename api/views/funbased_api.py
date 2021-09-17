from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Article
from api.serializers import ArticleSerializer


@api_view(["GET", "POST"])
def art_list_fun_api(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serialize_data = ArticleSerializer(articles, many=True)
        return Response(data=serialize_data.data)

    elif request.method == "POST":
        serialize_data = ArticleSerializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def art_detail_fun_api(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialize_data = ArticleSerializer(article)
        return Response(serialize_data.data, status=status.HTTP_302_FOUND)

    elif request.method == "PUT":
        serialize_data = ArticleSerializer(article, data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
