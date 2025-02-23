from django.db import models
from tailor.models import Tailor
from order.models import Order
from shop.models import Shop

# Create your models here.
class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    T_id=models.ForeignKey(Tailor,on_delete=models.CASCADE, related_name='products')
    O_id=models.ForeignKey(Order,on_delete=models.CASCADE, related_name='products')
    shop_id=models.ForeignKey(Shop,on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return self.name