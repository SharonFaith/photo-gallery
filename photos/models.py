from django.db import models
import datetime as dt

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

class Image(models.Model):
    #image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='other')
    location = models.ForeignKey(Location, on_delete=models.RESTRICT, default='other')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name