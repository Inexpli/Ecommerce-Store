from django.test import TestCase
from store.models import Category, Product

'''
Command to run the test properly:

coverage run --omit='*/venv/*' manage.py test

'''


class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')


    def test_category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data),'django')


class TestProductModel(TestCase):
    
    def setUp(self):
        Category.objects.create(name='runningshoes', slug='runningshoes')
        self.data1 = Product.objects.create(category_id=1, title='ultraboost', slug='ultraboost', price='20.00', image='django')
    
    def test_product_model_entry(self):
        data = self.data1
        self.assertEqual(str(data),'ultraboost')
