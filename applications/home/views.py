# -*- coding: utf-8 -*-
# django
from django.views.generic import ListView
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
)
from django.core.urlresolvers import reverse_lazy, reverse

#app home
from .models import Category, Entry
from .forms import BuscarForm


class IndexView(TemplateView):
    """ vista que carga pantalla principal """
    template_name = 'home/index.html'


class EntryListView(ListView):
    """vista que lista entradas"""
    context_object_name = 'entradas'
    paginate_by = 8
    template_name = 'home/list_entrada.html'

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.order_by('name')
        return context

    def get_queryset(self):
        return Entry.objects.order_by('-created')


class EntryFilterView(ListView):
    """vista que lista entradas por un filtro"""
    context_object_name = 'entradas'
    paginate_by = 8
    template_name = 'home/filtro.html'

    def get_context_data(self, **kwargs):
        context = super(EntryFilterView, self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.order_by('name')
        context['categoria'] = self.kwargs.get('filtro', 0)
        return context

    def get_queryset(self):
        categoria = self.kwargs.get('filtro', 0)
        return Entry.objects.filter(
            category__name=categoria,
        )


class EntryDetailView(DetailView):
    """vista que muetra el detalle de una entrada"""
    model = Entry
    template_name = 'home/detail_entrada.html'


class EntryBuscarListView(ListView):
    """vista que busca una entrada"""
    context_object_name = 'entradas'
    paginate_by = 8
    template_name = 'home/list_entrada.html'

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['form'] = BuscarForm
        return context

    def get_queryset(self):
        q = self.request.GET.get("buscar", '')
        return Entry.objects.filter(
            title=q,
        )


# class SugerenciaCreateView(CreateView):
#     model = Sugerencia
#     form_class = SugerenciaForm
#     success_url = '.'
#     template_name = 'home/add_sugerencia.html'
