from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Article(models.Model): 
    images = models.ImageField(null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
