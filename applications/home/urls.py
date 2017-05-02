# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    url(
        r'^$',
        views.IndexView.as_view(),
        name="inicio"
    ),
    url(
        r'^entrada/lista-entradas/$',
        views.EntryListView.as_view(),
        name="entrada-lista"
    ),
    #url para mostrar resultdos de filtro
    url(
        r'^lista-entradas-por/(?P<filtro>[-\w]+)/$',
        views.EntryFilterView.as_view(),
        name="entrada-filtro"
    ),
    url(
        r'^entrada/(?P<slug>[-\w]+)/$',
        views.EntryDetailView.as_view(),
        name="entrada-detalle"
    ),
]
