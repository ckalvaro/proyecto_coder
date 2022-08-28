from django.shortcuts import render
from django.http import HttpResponse
from AppNegocio.forms import FormularioNegocio, FormularioEmpleado, FormularioProducto
from .models import *

# Create your views here.
def inicio(request):
    return render(request, 'AppNegocio/padre.html')

def formulario_negocio(request):
    if request.method == 'POST':
        miFormularioNegocio = FormularioNegocio(request.POST)
        if miFormularioNegocio.is_valid():
            infoFormularioNegocio = miFormularioNegocio.cleaned_data
            nombre = infoFormularioNegocio.get('nombre')
            rubro = infoFormularioNegocio.get('rubro')
            direccion = infoFormularioNegocio.get('direccion')
            codigo_postal = infoFormularioNegocio.get('codigo_postal')
            negocio1 = Negocio(nombre = nombre, rubro = rubro, direccion = direccion, codigo_postal = codigo_postal)
            negocio1.save()
            mensaje = "Carga exitosa"
            return render(request, 'AppNegocio/hijo.html', {"mensaje":mensaje})
        else:
            mensaje = "Formulario Inválido"
            return render(request, 'AppNegocio/hijo.html', {"mensaje":mensaje})
    else:
        
        miFormularioNegocio = FormularioNegocio()
    return render(request, 'AppNegocio/hijo.html', {"miFormularioNegocio":miFormularioNegocio})

def buscar_negocio(request):
    if request.method == 'POST':
        nombre_negocio = request.POST["nombre"]
        negocios_buscados = Negocio.objects.filter(nombre__icontains = nombre_negocio)
        return render (request, "AppNegocio/resultado_negocios.html", {"negocios": negocios_buscados})
    else:
        return render(request, 'AppNegocio/buscar_negocios.html')
