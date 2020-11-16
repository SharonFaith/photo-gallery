from django.test import TestCase
from .models import Image, Location, Category
import datetime as dt
# Create your tests here.

class CategoryTestClass(TestCase):

    #set up method
    def setUp(self):
       self.new = Category(name = 'travel')

    def test_instance(self):

        self.assertTrue(isinstance(self.new, Category))

    def test_save_method(self):
        self.new.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.new.save_category()
        categ2= Category(name = 'food')
        categ2.save_category()
        categs  = Category.objects.all()
        print(categs)
        categ2.delete_category()
        categs  = Category.objects.all()
        print(categs)
        self.assertTrue(len(categs) == 1)

    def test_update_category(self):
        self.new.save_category()
        categ2= Category(name = 'food')
        categ2.save_category()
        print(categ2.id)
        Category.update_category(5, 'crops')

       
        
        
        self.assertEqual(Category.objects.filter(id = 5).first().name, 'crops')

class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
       self.place = Location(location_name = 'kile')

    def test_instance(self):

        self.assertTrue(isinstance(self.place, Location))

    def test_save_location(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_category(self):
        self.place.save_location()
        place2= Location(location_name = 'kili')
        place2.save_location()
        
        place2.delete_location()
        places = Location.objects.all()
        print(places)
        self.assertTrue(len(places) == 1)