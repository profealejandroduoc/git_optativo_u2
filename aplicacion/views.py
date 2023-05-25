from django.shortcuts import render
from .models import Persona

# Create your views here.
def index(request):
    people=Persona.objects.all()

    ctx={
        "lista":people
    }
    return render(request,"aplicacion/index.html",ctx)