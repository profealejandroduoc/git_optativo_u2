from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)


    def __str__(self):
        return self.nombre + " " + self.apellido