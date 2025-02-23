from django.db import models
from customer.models import Customer
from product.models import Product
from shop.models import Shop

# Create your models here.
class Order(models.Model):
    O_id = models.AutoField(primary_key=True)
    C_id=models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='orders')
    p_id=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='orders')
    shop_id=models.ForeignKey(Shop,on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField()
    order_status = models.CharField(max_length=200)
    order_total = models.FloatField()
    order_description = models.TextField()
    
    def __str__(self):
        return self.order_id
    