from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio_proyecto.html')