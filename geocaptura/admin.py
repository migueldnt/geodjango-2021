#from django.contrib import admin
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Reporte,AreaAtendida

class ReportesAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (18.8917,-99.1479),
        'DEFAULT_ZOOM': 8,
        'SRID': 4326
    }

# Register your models here.
admin.site.register(Reporte,ReportesAdmin)
admin.site.register(AreaAtendida,ReportesAdmin)