from django.db import models
from randomslugfield import RandomSlugField

class Story(models.Model):
    title = models.CharField(max_length=255)
    slug = RandomSlugField(length=10)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title