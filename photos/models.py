from django.db import models
import datetime as dt

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, update):
        category_to_update = cls.objects.filter(id = id)
        category_to_update.update(name = update)
        


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, update):
        location_to_update = cls.objects.filter(id = id)
        location_to_update.update(location_name = update)

class Image(models.Model):
    #image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name