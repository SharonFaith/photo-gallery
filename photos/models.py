from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    #image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
#    category = models.ForeignKey(Category, on_delete=models.CASCADE)
#    location = models.ForeignKey(Editor, on_delete=models.RESTRICT)
    upload_date = models.DateTimeField(auto_now_add=True)

