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
    url(
        r'^entrada/buscar/$',
        views.EntryBuscarListView.as_view(),
        name="entrada-buscar"
    ),
    #url para mostrar resultdos de filtro
    url(
        r'^lista-de-entradas-segun-flitro/(?P<filtro>[-\w]+)/$',
        views.EntryFilterView.as_view(),
        name="entrada-filtro"
    ),
    url(
        r'^entrada/(?P<slug>[-\w]+)/$',
        views.EntryDetailView.as_view(),
        name="entrada-detalle"
    ),
    url(
        r'^agregar-sugencia/$',
        views.SugerenciaCreateView.as_view(),
        name="sugerencia-add"
    ),
    url(
        r'^lista-de-sugerencias/$',
        views.ListaSugerenciaView.as_view(),
        name="sugerencia-list"
    ),
    url(
        r'^entradas-con-suscripcion/$',
        views.ListaConFormView.as_view(),
        name="entrada-suscripcion"
    ),

]
