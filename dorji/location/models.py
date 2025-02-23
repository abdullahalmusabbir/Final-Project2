from django.db import models
from customer.models import Customer
from tailor.models import Tailor

# Create your models here.
class Location(models.Model):
    L_id = models.AutoField(primary_key=True)
    C_id=models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='locations')
    T_id=models.ForeignKey(Tailor,on_delete=models.CASCADE, related_name='locations')
    city = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    road = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    
    def __str__(self):
        return self.postal_code