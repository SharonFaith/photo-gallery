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