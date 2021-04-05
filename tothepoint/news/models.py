from django.db import models
from django.urls import reverse


# Create your models here.
class Headlines(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    text = models.TextField(null=True)
    image = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title
