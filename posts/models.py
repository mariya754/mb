from django.db import models

class Post(models.Model):

    text = models.TextField()
    author = models.TextField(default="unknown")
    title = models.TextField(default='')

    def __str__(self):
        """ Строковое отображение модели"""
        return self.text[:50]