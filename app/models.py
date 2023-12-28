from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=40)
    data = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
