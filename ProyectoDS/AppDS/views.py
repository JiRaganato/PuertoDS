from django.shortcuts import render
from django.http import HttpResponse
from AppDS.models import Chofer

# Create your views here.

def chofer(self):
    chofer = Chofer(nombre= 'Gustavo', apellido= 'Barraza', transporte= 'Loginter', contacto= 'barrazaloginter@gmail.com')
    
    chofer.save()

    documento = f'Chofer {chofer.apellido}, {chofer.nombre}, transporte: {chofer.transporte}'

    return HttpResponse(documento)

def inicio(request):

    return render(request, "AppDS/inicio.html")

def packinglist(request):

    return render(request, "AppDS/PackingList.html")

def informes(request):

    return render(request, "AppDS/informes.html")

def choferes(request):

    return render(request, "AppDS/choferes.html")


    
    