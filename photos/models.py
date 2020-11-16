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
    def update_location(cls, name, update):
        location_to_update = cls.objects.filter(location_name = name)
        location_to_update.update(location_name = update)

class Image(models.Model):
    image = models.ImageField(upload_to = 'uploads/', default = 'pics')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image_name(cls, image_name, update):
        image_to_update = cls.objects.filter(image_name = image_name)
        image_to_update.update(image_name = update)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id = id)
        
        return image

    @classmethod
    def search_image(cls, category):
        pictures = cls.objects.filter(category__icontains = category)
        return pictures
    
    @classmethod
    def filter_by_location(cls, location):
        place = Location.objects.filter(location_name = location).first()

        
        pictures = cls.objects.all()
        picture_array = empty
        for picture in pictures:
            if picture.location == place.id:
                picture_array.insert(0, picture)

        return picture_array