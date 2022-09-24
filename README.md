# GEODJANGO 2021

### Tutorial del proyecto

#### instalar virtualenv  y crear el entorno
(omitir si ya se tiene preparado el entorno de python)

```bash
pip install virtualenv 
#o  
pip3 install virtualenv

crear el entorno

mkdir geodjango-2021
cd geodjango-2021
virtualenv env
source env/bin/activate
```

#### instalar django y crear el proyecto 

```
pip install django
pip install psycopg2-binary
django-admin startproject colaboracion_geoespacial $(pwd)
```

probar que django ya este funcionando

```
python manage.py runserver
```

#### aplicacion y crear los modelos

```
python manage.py startapp geocaptura
```

agregar esto a las apps de settings.py

```
'django.contrib.gis',
'geocaptura'
```

#### conectar la base de datos

Previamente contar una base de datos alcanzable por el proyecto de django.

crear el archivo .env, es una copia de .env-example, llenarlo con los datos correctos.

modificar settings.py para apuntar al archivo .env

ejecutar

```sh
export $(cat .env | xargs)
```

```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

#### agregar el nuevo modelo al Admin

en admin.py agregar
```python
from django.contrib.gis import admin
from .models import Reporte,AreaAtendida

admin.site.register(Reporte,ReportesAdmin)
admin.site.register(AreaAtendida,ReportesAdmin)
```

instalar leaflet para ver  mas presentables los  mapas

```
pip install django-leaflet
```
agregar leaflet a las apps de settings.py

en 'admin.py' agregar


pasarle algunos parametros a los mapas de leaflet

```python
from leaflet.admin import LeafletGeoAdmin

class ReportesAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (18.8917,-99.1479),
        'DEFAULT_ZOOM': 8,
        'SRID': 4326
    }
```

**Hasta aqui ya se puede capturar informacion en el admin**

### Crear nuestras propias vistas
El admin es muy practico y facil de usar, pero ya que el admin tiene muy pocas opciones de configuracion , seguramente sera necesario hacer vistas personalizadas de las acciones que requerimos hacer

#### Un formulario fuera del admin

Crear el archivo forms.py y crear un formulario con el widget de leaflet de edicion de geometria

```python
from django import forms

from .models import Reporte

from leaflet.forms.widgets import LeafletWidget

class CapturaCiudadano(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ('ubicacion','descripcion','tipo')
        widgets = {'ubicacion': LeafletWidget(attrs={
            'settings_overrides': {
                'DEFAULT_CENTER': (18.8917,-99.1479),
                'DEFAULT_ZOOM': 8,
            }
        })}

```
agregar templates/geocaptura/captura.html , es un archivo html normal, solo hay que agregar informacion 

```html
{% load leaflet_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
    {% leaflet_js plugins="forms" %}
    {% leaflet_css plugins="forms" %}
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Captura de reportes</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
</head>
<body>
    <form method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

en views.py agregar

```python
from django.shortcuts import render
from django.http import HttpResponse

from .forms import CapturaCiudadano

def capturaCiudadano(request):
    if request.method == 'POST':
        form = CapturaCiudadano(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Se guardo correctamente")

    else:
        form = CapturaCiudadano()
    
    return render(request,'geocaptura/captura.html',{'form':form})

```

en urls.py, dentro  de urlpatterns agregar

```python
path("captura-ciudadano/",capturaCiudadano)
```

#### Un servicio de los Reportes
en views.py agregar 

```python
def geoservicioReportes(request):
    reportes = Reporte.objects.all()
    geojson=serialize("geojson",reportes,geometry_field="ubicacion")
    response=HttpResponse(geojson,content_type="application/json")
    response["Access-Control-Allow-Origin"]="*"
    return response
```

en urls.py, dentro  de urlpatterns agregar

```python
path("geoservicio-reportes/",geoservicioReportes),
```

#### Un servicio de las areas atendidas

(muy similar al servicio de reportes)

#### Un mapa que muestre la informacion capturada

agregar templates/mapa.html


```html
{% load leaflet_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapa</title>
    {% leaflet_js %}
    {% leaflet_css %}
    <style>
        .leaflet-container { height: 100vh; }
    </style>
</head>
<body>
    {% leaflet_map "main" %}
    <script>
        var dataurl = '/geoservicio-reportes/';
  
        window.addEventListener("map:init", function (event) {
          var map = event.detail.map;
          map.setView([18.8917,-99.1479], 8);
          // Download GeoJSON data with Ajax
          fetch(dataurl)
            .then(function(resp) {
              return resp.json();
            })
            .then(function(data) {
              L.geoJson(data, {
                onEachFeature: function onEachFeature(feature, layer) {
                  var props = feature.properties;
                  
                  layer.bindPopup(`${props.descripcion}`);
              },
              //style:function(feature){ return {color:'red'}}
            }).addTo(map);
            });
        });
      </script>
</body>
</html>
```

agregar en views.py

```python
def mapaGobierno(request):
    return render(request,'geocaptura/mapa.html',{})
```

en urls.py

```python
path("mapa-gobierno/",mapaGobierno),
```