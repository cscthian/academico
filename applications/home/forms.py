# -*- encoding: utf-8 -*-
from django import forms

from .models import Sugerencia

class BuscarForm(forms.Form):
    buscar = forms.CharField(
        label='Search',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'busca una entrada ..',
            }
        )
    )


class SugerenciaForm(forms.ModelForm):

    class Meta:
        model = Sugerencia
        fields = (
            'title',
            'contenido',
            'name',
            'email',
        )


# class SuscripcionForm(forms.Form):
#     first_name = forms.CharField(
#         label='Su Nombre',
#         max_length='70',
#         required=False,
#     )
#     last_name = forms.CharField(
#         label='Su Apellido',
#         max_length='50', required=False)
#     email = forms.EmailField(
#         label='Su E-mail',
#         max_length='70',
#         required=False,
#     )
