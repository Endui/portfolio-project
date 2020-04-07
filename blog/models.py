from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
