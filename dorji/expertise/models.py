from django.db import models

# Create your models here.
class Expertise(models.Model):
    E_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    level=models.CharField(max_length=200)
    
    def __str__(self):
        return self.type