from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=250)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    body = models.TextField()