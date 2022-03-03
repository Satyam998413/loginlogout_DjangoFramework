from email.mime import image
from django.db import models

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    image=models.ImageField(upload_to="static/blog/images",default="")

    def __str__(self):
        return self.title + " by " + self.author