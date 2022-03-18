from django.db import models

class Post(models.Model):
    python = models.CharField(max_length=150)
    java = models.CharField(max_length=100)
    javascript = models.CharField(max_length=160)


