# -*- encoding: utf-8 -*-
from django import forms

from .models import Sugerencia, Subscription

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


class SuscripcionForm(forms.Form):
    first_name = forms.CharField(
        label='Su Nombre',
        max_length='70',
        required=False,
    )
    last_name = forms.CharField(
        label='Su Apellido',
        max_length='50', required=False)
    email = forms.EmailField(
        label='Su E-mail',
        max_length='70',
        required=False,
    )


class SuscripcionForm2(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = (
            'first_name',
            'last_name',
            'email',
        )


# class ContactoForm(forms.ModelForm):

#     class Meta:
#         model = Zone
#         fields = (
#             'name',
#         )
#         widgets = {
#             'name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Nombre de ...',
#                 }
#             ),
#         }

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if Zone.objects.filter(name=name, state=False).count() > 0:
#             msj = 'el nombre de zona ya existe'
#             self.add_error('name', msj)
#         return name