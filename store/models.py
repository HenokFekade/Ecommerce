from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Catagory(models.Model):
    name = models.CharField(max_length=255,)
    slug = models.SlugField(unique=True, max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Catagories'



class Product(models.Model):
    catagory = models.ForeignKey(Catagory, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)



