from django.db import models

class Doctor(models.Model):
    image = models.ImageField(upload_to='doctors/') 
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11,default='00000000000')
    specialization = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    working_hours = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
