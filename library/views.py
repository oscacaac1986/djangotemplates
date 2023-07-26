
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return HttpResponse("<h1>Inicio</h1>")

def nosotros(request):
    return render(request, 'pages/nosotros.html')