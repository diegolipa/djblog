from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,     null=True)
    body = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return '%s- %s' % (self.title, self.body)


class Commentary(models.Model):

    commentary = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentarys"

    def __str__(self):
        return '%s - %s' % (self.commentary, self.post)