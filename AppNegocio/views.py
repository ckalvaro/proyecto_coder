from django.shortcuts import render
from django.http import HttpResponse
from AppNegocio.forms import FormularioNegocio, FormularioEmpleado, FormularioProducto
from .models import *

# Create your views here.
def inicio(request):
    return render(request, 'AppNegocio/inicio_negocios.html')

def formulario_negocio(request):
    if request.method == 'POST': #SI EL METODO ES POST
        miFormularioNegocio = FormularioNegocio(request.POST)
        if miFormularioNegocio.is_valid():
            infoFormularioNegocio = miFormularioNegocio.cleaned_data
            nombre = infoFormularioNegocio.get('nombre')
            rubro = infoFormularioNegocio.get('rubro')
            direccion = infoFormularioNegocio.get('direccion')
            codigo_postal = infoFormularioNegocio.get('codigo_postal')
            negocio1 = Negocio(nombre = nombre, rubro = rubro, direccion = direccion, codigo_postal = codigo_postal)
            negocio1.save()
            mensaje = "¡Carga exitosa!"
            return render(request, 'AppNegocio/form_negocio.html', {"mensaje":mensaje})
        else:
            mensaje = "Formulario Inválido"
            return render(request, 'AppNegocio/form_negocio.html', {"mensaje":mensaje})
    else: #si el método es GET
        
        miFormularioNegocio = FormularioNegocio()
    return render(request, 'AppNegocio/form_negocio.html', {"miFormularioNegocio":miFormularioNegocio})

def buscar_negocio(request):
    if request.method == 'POST':
        nombre_negocio = request.POST["nombre"]
        negocios_buscados = Negocio.objects.filter(nombre__icontains = nombre_negocio)
        return render (request, "AppNegocio/resultado_negocio.html", {"negocios": negocios_buscados})
    else:
        return render(request, 'AppNegocio/buscar_negocio.html')


def formulario_empleado(request):
    if request.method == 'POST':
        miFormularioEmpleado = FormularioEmpleado(request.POST)
        if miFormularioEmpleado.is_valid():
            infoFormularioEmpleado = miFormularioEmpleado.cleaned_data
            nombre = infoFormularioEmpleado.get('nombre')
            apellido = infoFormularioEmpleado.get('apellido')
            sector = infoFormularioEmpleado.get('sector')
            edad = infoFormularioEmpleado.get('edad')
            empleado1 = Empleado(nombre = nombre, apellido = apellido, sector = sector , edad = edad )
            empleado1.save()
            mensaje = "¡Carga exitosa!"
            return render(request, 'AppNegocio/form_empleado.html', {"mensaje":mensaje})
        else:
            mensaje = "Formulario Inválido"
            return render(request, 'AppNegocio/form_empleado.html', {"mensaje":mensaje})
    else:
        
        miFormularioEmpleado = FormularioEmpleado()
    return render(request, 'AppNegocio/form_empleado.html', {"miFormularioEmpleado":miFormularioEmpleado})

def buscar_empleado(request):
    if request.method == 'POST':
        nombre_empleado = request.POST["nombre"]
        empleados_buscados = Empleado.objects.filter(nombre__icontains = nombre_empleado)
        return render (request, "AppNegocio/resultado_empleado.html", {"empleados": empleados_buscados})
    else:
        return render(request, 'AppNegocio/buscar_empleado.html')

def formulario_producto(request):
    if request.method == 'POST': #SI EL METODO ES POST
        miFormularioProducto = FormularioProducto(request.POST)
        if miFormularioProducto.is_valid():
            infoFormularioProducto = miFormularioProducto.cleaned_data
            nombre = infoFormularioProducto.get('nombre')
            precio = infoFormularioProducto.get('precio')
            cantidad = infoFormularioProducto.get('cantidad')
            categoria = infoFormularioProducto.get('categoria')
            producto1 = Producto(nombre = nombre, precio = precio, cantidad = cantidad, categoria = categoria)
            producto1.save()
            mensaje = "¡Carga exitosa!"
            return render(request, 'AppNegocio/form_producto.html', {"mensaje":mensaje})
        else:
            mensaje = "Formulario Inválido"
            return render(request, 'AppNegocio/form_producto.html', {"mensaje":mensaje})
    else: #si el método es GET
        miFormularioProducto = FormularioProducto()
    return render(request, 'AppNegocio/form_producto.html', {"miFormularioProducto":miFormularioProducto})

def buscar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST["nombre"]
        productos_buscados = Producto.objects.filter(nombre__icontains = nombre_producto)
        return render (request, "AppNegocio/resultado_producto.html", {"productos": productos_buscados})
    else:
        return render(request, 'AppNegocio/buscar_producto.html')
