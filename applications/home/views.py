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
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy, reverse

#app home
from .models import Category, Entry, Sugerencia
from .forms import BuscarForm, SugerenciaForm


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
    #paginate_by = 8
    template_name = 'home/lista.html'

    def get_context_data(self, **kwargs):
        context = super(EntryBuscarListView, self).get_context_data(**kwargs)
        context['form'] = BuscarForm
        return context

    def get_queryset(self):
        q = self.request.GET.get("buscar", '')
        return Entry.objects.filter(
            title__icontains=q,
        )


class SugerenciaCreateView(CreateView):
    model = Sugerencia
    form_class = SugerenciaForm
    success_url = reverse_lazy('home_app:sugerencia-list')
    template_name = 'home/add_sugerencia.html'


class ListaSugerenciaView(ListView):
    context_object_name = 'sugerencias'
    template_name = 'home/lista_sugerencia.html'

    def get_queryset(self):
        return Sugerencia.objects.all()


# class ListaConFormView(FormMixin, ListView):
#     context_object_name = 'entree_list'
#     template_name = 'home/lista_form.html'
#     paginate_by = 4
#     form_class = SuscripcionForm
#     success_url = reverse_lazy('home_app:entrada-lista')
#
#     def get_queryset(self):
#         return Entry.objects.order_by('-created')
#
#     def get_context_data(self, **kwargs):
#         context = super(ListaConFormView, self).get_context_data(**kwargs)
#         context['form'] = self.get_form()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         first_name = form.cleaned_data['first_name']
#         last_name = form.cleaned_data['last_name']
#         email = form.cleaned_data['email']
#         #validamos si el email existe
#         if Subscription.objects.filter(email=user).count()==0:
#             subscription = Subscription(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#             )
#             subscription.save()
#         return super(ListaConFormView, self).form_valid(form)
