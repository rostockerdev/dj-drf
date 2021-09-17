from rest_framework import serializers

from api.models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    author = serializers.CharField(max_length=128)
    email = serializers.EmailField(max_length=128)
    published_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.email = validated_data.get("email", instance.email)
        instance.published_at = validated_data.get(
            "published_at", instance.published_at
        )
        instance.save()
        return instance


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["pk", "title", "author", "email", "published_at"]
