from django.contrib import admin
from django.urls import path
from AppNegocio.views import inicio, formulario_negocio, buscar_negocio

urlpatterns = [
    path('', inicio, name='inicio_app'),
    path('form_negocio/', formulario_negocio, name='formulario_negocio'),
    path('buscar_negocio/', buscar_negocio, name='buscar_negocio'),
]
