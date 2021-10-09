from django.urls import path, include

from .views import holaMundo, capturaCiudadano, geoservicioAreas, geoservicioReportes,mapaGobierno

urlpatterns = [
    path("hola/", holaMundo),
    path("captura-ciudadano/",capturaCiudadano),
    path("geoservicio-reportes/",geoservicioReportes),
    path("geoservicio-areas/",geoservicioAreas),
    path("mapa-gobierno/",mapaGobierno),
]