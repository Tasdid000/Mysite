from django.db import models


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

class cv(models.Model):
    sno = models.AutoField(primary_key=True)
    cv = models.FileField(upload_to="cv/", default="")
    
class certificate(models.Model):
    sno = models.AutoField(primary_key=True)
    certificate = models.ImageField(upload_to='certificate', default='')