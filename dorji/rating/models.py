from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.
class Rating(models.Model):
    R_id = models.AutoField(primary_key=True)
    C_id=models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='ratings')
    P_id=models.ForeignKey(Product,on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()
    review = models.CharField(max_length=200)
    
    def __str__(self):
        return self.rating