from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#tabla usuarios
class usuarios(models.Model):
    usuario=models.AutoField(primary_key=True)
    pasword=models.CharField(max_length=8)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField(max_length=10)
    
    def __str__(self): 
        return self.usuario
    
    #tabla productos
    
class productos (models.Model):
    id_producto=models.IntegerField(primary_key=True)
    nombre=models.TextField(max_length=60)
    precio=models.DecimalField(max_digits=10, decimal_places=3)
    stock=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='image/',)
    
    def __str__(self): 
        return self.nombre