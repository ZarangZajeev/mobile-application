from django.db import models

# Create your models here.

class Mobiles(models.Model):
    name=models.CharField(max_length=100,unique=True)
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=100)
    specs=models.CharField(max_length=100)
    display=models.CharField(max_length=100)
    picture=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name