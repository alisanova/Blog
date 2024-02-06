from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to="images/", default="images/default.jpg")


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Categories"