from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=150, default="por ahi 123")


    def __str__(self):
        return self.nombre + " " + self.apellido
    

class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    tipo=models.CharField(max_length=25)
    propietario=models.ForeignKey(Persona,models.PROTECT)