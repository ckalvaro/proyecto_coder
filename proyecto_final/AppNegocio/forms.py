from django import forms

class FormularioNegocio(forms.Form):
    nombre = forms.CharField(max_length=50)
    rubro = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=100)
    codigo_postal = forms.IntegerField()

class FormularioProducto(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()
    cantidad = forms.IntegerField()
    categoria = forms.CharField(max_length=50)

class FormularioEmpleado(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    sector = forms.CharField(max_length=50)
    edad = forms.IntegerField()