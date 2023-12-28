from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
