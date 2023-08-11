from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class portfolio(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio', default='')
    content = models.TextField()
    slug = models.CharField(max_length=130)

    def __str__(self):
        return self.title + ' by ' + self.content[0:30]
    
class allimage(models.Model):
    sno = models.AutoField(primary_key=True)
    all_image = models.ImageField(upload_to='portfolio', default='')