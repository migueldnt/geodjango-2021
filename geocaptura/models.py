#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Reporte(models.Model):
    id = models.BigAutoField(primary_key=True)
    ubicacion = models.PointField()
    descripcion = models.TextField(default="")
    tipo = models.CharField(max_length=20, choices=[
        ("bache","Bache"),
        ("falta_alumbrado","Falta de alumbrado"),
        ("semaforo","Falla de semaforo"),
        ("otros","Otros")
        ],default="otros")
    status = models.CharField(max_length=20, choices=[
        ("pendiente","pendiente"),
        ("resuelto","resuelto"),
        ("en_proceso","en_proceso")
        ],default="pendiente")
    fecha = models.DateTimeField(null=True)


class AreaAtendida(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.PolygonField()
    descripcion = models.TextField(default="")