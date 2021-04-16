from django.contrib import admin
from store.models import Catagory, Product

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'is_active', 'updated', 'created']
    prepopulated_fields = {'slug': ('title',)}
    filter = ['in_stock', 'is_active',]
    list_editable = ['in_stock', 'price',]
