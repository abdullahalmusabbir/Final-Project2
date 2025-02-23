from django.db import models

# Create your models here.
class Size(models.Model):
    S_id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=200)
    size_chart = models.CharField(max_length=200)
    range=models.CharField(max_length=200)
    
    def __str__(self):
        return self.size