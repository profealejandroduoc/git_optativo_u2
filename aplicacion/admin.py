from django.contrib import admin
from .models import Mascota, Persona

# Register your models here.
class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido"]
    list_editable=["nombre","apellido"]

    class meta:
        model=Persona

admin.site.register(Persona,admPersona)

class admMascota(admin.ModelAdmin):
    list_display=["id","nombre","tipo","propietario"]
    list_editable=["nombre","tipo","propietario"]

    class meta:
        model=Mascota


admin.site.register(Mascota,admMascota)