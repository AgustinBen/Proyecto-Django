from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.



def index(request):
    return render(request, 'Tienda/index.html')


def lista_productos(request):
    return render(request, 'Tienda/lista_productos.html')