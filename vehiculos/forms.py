from django import forms
from .models import Vehiculo


class VehiculoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)
        self.fields['precio'].widget.attrs['class'] = 'form-control'
        self.fields['modelo'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Vehiculo
        exclude = []
