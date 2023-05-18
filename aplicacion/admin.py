from django.contrib import admin
from .models import Persona

# Register your models here.
class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido"]
    list_editable=["nombre","apellido"]

    class meta:
        model=Persona

admin.site.register(Persona,admPersona)