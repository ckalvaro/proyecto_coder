from django.contrib import admin
from django.urls import path
from AppNegocio.views import inicio, formulario_negocio

urlpatterns = [
    path('', inicio, name='inicio_app'),
    path('form_negocio/', formulario_negocio, name='formulario_negocio'),
]
