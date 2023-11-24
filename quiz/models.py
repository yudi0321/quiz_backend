from django.db import models


# Create your models here.
class Quiz(models.Model):
    title    = models.CharField(max_length=300)
    body     = models.TextField()
    answer   = models.IntegerField()
    category = models.CharField(max_length=100, default="")
