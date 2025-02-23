from django.db import models
from tailor.models import Tailor
from rating.models import Rating
from location.models import Location

# Create your models here.
class Shop(models.Model):
    S_id = models.AutoField(primary_key=True)
    T_id=models.ForeignKey(Tailor,on_delete=models.CASCADE, related_name='shops')
    R_id=models.ForeignKey(Rating,on_delete=models.CASCADE, related_name='shops')
    L_id=models.ForeignKey(Location,on_delete=models.CASCADE, related_name='shops')
    S_name = models.CharField(max_length=200)
    S_email = models.CharField(max_length=200)
    S_description = models.TextField()
    
    def __str__(self):
        return self.S_name