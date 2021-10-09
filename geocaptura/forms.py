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
