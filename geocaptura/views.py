from django.shortcuts import render
from django.http import HttpResponse

from .forms import CapturaCiudadano

from .models import Reporte,AreaAtendida
from django.core.serializers import serialize

# Create your views here.
def holaMundo(request):
    return HttpResponse("Hola mundo")


def capturaCiudadano(request):
    if request.method == 'POST':
        form = CapturaCiudadano(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Se guardo correctamente")

    else:
        form = CapturaCiudadano()
    
    return render(request,'geocaptura/captura.html',{'form':form})


def geoservicioReportes(request):
    reportes = Reporte.objects.all()
    geojson=serialize("geojson",reportes,geometry_field="ubicacion")
    response=HttpResponse(geojson,content_type="application/json")
    response["Access-Control-Allow-Origin"]="*"
    return response

def geoservicioAreas(request):
    reportes = AreaAtendida.objects.all()
    geojson=serialize("geojson",reportes,geometry_field="area")
    response=HttpResponse(geojson,content_type="application/json")
    response["Access-Control-Allow-Origin"]="*"
    return response

def mapaGobierno(request):
    return render(request,'geocaptura/mapa.html',{})