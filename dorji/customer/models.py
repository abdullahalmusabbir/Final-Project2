from django.db import models
from order.models import Order
from location.models import Location
from size.models import Size

# Create your models here.
class Customer(models.Model):
    C_id = models.AutoField(primary_key=True)
    O_id=models.ForeignKey(Order,on_delete=models.CASCADE, related_name='customers')
    L_id=models.ForeignKey(Location,on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender=models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    size= models.ForeignKey(Size,on_delete=models.CASCADE, related_name='customers')
    
    def __str__(self):
        return self.name