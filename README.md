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

agregar admin.site.register, y from django.contrib.gis import admin (ver el archivo geocaptura/admin.py)


instalar leaflet para algo mas presentable de mapas

```
pip install django-leaflet
```
agregar leaflet a las apps de settings.py

---

### Crear nuestras propias vistas

