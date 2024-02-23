from django.db import models

# Create your models here.
class POST(models.Model):
    title = models.CharField(max_lengs=255)
    slug = models.SlugField()
    intro = models.TextField()
    body =  models.TextField()
    posted_data = models.DataTimeField(auto_now_add=True)
