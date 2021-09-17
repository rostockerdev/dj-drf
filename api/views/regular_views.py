from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from api.models import Article
from api.serializers import ArticleSerializer


@csrf_exempt
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serialize_data = ArticleSerializer(articles, many=True)
        return JsonResponse(data=serialize_data.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serialize_data = ArticleSerializer(data=data)
        if serialize_data.is_valid():
            serialize_data.save()
            return JsonResponse(serialize_data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "GET":
        serialize_data = ArticleSerializer(article)
        return JsonResponse(serialize_data.data, status=status.HTTP_302_FOUND)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serialize_data = ArticleSerializer(article, data=data)
        if serialize_data.is_valid():
            serialize_data.save()
            return JsonResponse(serialize_data.data, status=status.HTTP_202_ACCEPTED)
        return JsonResponse(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
