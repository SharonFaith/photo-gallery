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
       
        categ2.delete_category()
        categs  = Category.objects.all()
        
        self.assertTrue(len(categs) == 1)

    def test_update_category(self):
        self.new.save_category()
        categ2= Category(name = 'food')
        categ2.save_category()
        
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

    def test_delete_location(self):
        self.place.save_location()
        place2= Location(location_name = 'kili')
        place2.save_location()
        
        place2.delete_location()
        places = Location.objects.all()
       
        self.assertTrue(len(places) == 1)

    def test_update_location(self):
         
        self.place.save_location()
        place2= Location(location_name = 'kili')
        place2.save_location()
        print(place2.id)
        Location.update_location(11, 'westlands')
        
        
        self.assertEqual(Location.objects.filter(id = 11).first().location_name, 'westlands')

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a category and saving it
        self.categ2= Category(name = 'food')
        self.categ2.save_category()

       
        # Creating a location and saving it
        self.place2= Location(location_name = 'kili')
        self.place2.save_location()

       

        #creating instance of image
        self.pic = Image(image_name = 'brown', image_description= 'A brown picture', category = self.categ2, location = self.place2 )
       
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()


    

    def test_instance(self):

        self.assertTrue(isinstance(self.pic, Image))

    def test_save_image(self):
        self.pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.pic.save_image()
        image2 = Image(image_name = 'red', image_description= 'A red picture', category = self.categ2, location = self.place2 ) 
        image2.save_image()
        
        image2.delete_image()
        images = Image.objects.all()
#        print(images)
        self.assertTrue(len(images) == 1)

    def test_update_image(self):
         
        self.pic.save_image()
#        print(self.pic.id)
        image2 = Image(image_name = 'red', image_description= 'A red picture', category = self.categ2, location = self.place2 ) 
        image2.save_image()
        print(image2.id)

#        print(Image.objects.all())

        Image.update_image_name(10, 'green')

        self.assertEqual(Image.objects.filter(id = 10).first().image_name, 'green')

    def test_get_image_by_id(self):

        self.pic.save_image()
        
        image2 = Image(image_name = 'red', image_description= 'A red picture', category = self.categ2, location = self.place2 ) 
        image2.save_image()
        print(image2.id)
        Image.get_image_by_id(4)

        self.assertEqual(Image.objects.filter(id = 4).first().image_name, 'red')

