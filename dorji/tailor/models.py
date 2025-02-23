from django.db import models
from location.models import Location
from shop.models import Shop
from rating.models import Rating
from expertise.models import Expertise

# Create your models here.
class Tailor(models.Model):
    T_id = models.AutoField(primary_key=True)
    shop_id=models.ForeignKey(Shop,on_delete=models.CASCADE, related_name='tailors')
    R_id=models.ForeignKey(Rating,on_delete=models.CASCADE, related_name='tailors')
    E_id=models.ForeignKey(Expertise,on_delete=models.CASCADE, related_name='tailors')
    T_name = models.CharField(max_length=200)
    T_email = models.CharField(max_length=200)
    T_phone = models.CharField(max_length=200)
    T_address = models.CharField(max_length=200)
    T_description = models.TextField()
    
    def __str__(self):
        return self.T_name