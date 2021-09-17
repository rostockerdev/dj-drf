from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
