# -*- encoding: utf-8 -*-
from django import forms

#from .models import Sugerencia

class BuscarForm(forms.Form):
    buscar = forms.CharField(
        label='Buscar',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'buscar por ..',
            }
        )
    )


# class SugerenciaForm(forms.ModelForm):
#
#     class Meta:
#         model = Sugerencia
#         fields = (
#             'title',
#             'contenido',
#             'email',
#         )
