from django.contrib import admin
from django.urls import path
from AppNegocio.views import inicio, formulario_negocio, buscar_negocio, formulario_empleado, buscar_empleado, formulario_producto, buscar_producto

urlpatterns = [
    path('', inicio, name='inicio_app'),
    path('form_negocio/', formulario_negocio, name='formulario_negocio'),
    path('buscar_negocio/', buscar_negocio, name='buscar_negocio'),
    path('form_empleado/',formulario_empleado,name='formulario_empleado'),
    path('buscar_empleado/',buscar_empleado,name='buscar_emmpleado'),
    path('form_producto/', formulario_producto, name='formulario_producto'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
]
