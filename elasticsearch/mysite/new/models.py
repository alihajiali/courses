from django.db import models

# Create your models here.
class InstagramUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hashtag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title