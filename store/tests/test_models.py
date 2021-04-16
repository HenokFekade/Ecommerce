from django.test import TestCase
from store.models import Product, Catagory
from django.contrib.auth.models import User


class TestCatagoryModel(TestCase):
    def setUp(self):
        self.data = Catagory.objects.create(name='django', slug='django')

    def test_catagory_model_entry(self):
        """
        test catagory model default name
        """
        self.assertEqual(str(self.data), self.data.name)


class TestProductModel(TestCase):
    def setUp(self):
        catagory = Catagory.objects.create(name='django', slug='django')
        user = User.objects.create(username='nani')

        self.data = Product.objects.create(catagory=catagory, created_by=user, description='django', title='django beginners', slug='django-beginner', price=29.04,)

    def test_product_model_entry(self):
        """
        test product model default name
        """
        self.assertEqual(str(self.data), self.data.title)