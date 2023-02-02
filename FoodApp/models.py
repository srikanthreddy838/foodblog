from django.db import models


class Destination(models.Model):
    name_1=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField() 
    price=models.BooleanField(default=False)
# Create your models here.
