from django.db import models
from .category import Category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=200 , default=0)
    image = models.ImageField(upload_to='uploads/products')

    @staticmethod
    def get_all_products():
        return Product.objects.all()