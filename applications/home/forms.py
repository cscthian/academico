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
