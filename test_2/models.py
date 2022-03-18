from django.db import models

class Comment(models.Model):
    positive_reviews = models.CharField(max_length=50)
    negative_feedback = models.CharField(max_length=40)

