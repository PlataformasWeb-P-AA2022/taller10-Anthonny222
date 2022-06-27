from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('barrios', views.listarBarrio, name = 'listadoBarrios'),
    path ('creacion/parroquia', views.crearParroquia, name='crearParroquia'),
    path ('creacion/barrio/parroquia/<int:id>', views.crearBarrioParroquia, name='crearBarrioParroquia'),
    path ('editar/parroquia/<int:id>', views.editarParroquia, name='editarParroquia'),
    path ('editar/barrio/<int:id>', views.editarBarrio, name='editarBarrio'),
]