from django.contrib import admin
from django.urls import path
from AppNegocio.views import inicio, formulario_negocio, buscar_negocio,formulario_empleado,buscar_empleado

urlpatterns = [
    path('', inicio, name='inicio_app'),
    path('form_negocio/', formulario_negocio, name='formulario_negocio'),
    path('buscar_negocio/', buscar_negocio, name='buscar_negocio'),
    path('form_empleado/',formulario_empleado,name='formulario_empleado'),
    path('buscar_empleado/',buscar_empleado,name='buscar_emmpleado'),
]
