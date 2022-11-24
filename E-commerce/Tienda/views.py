from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import date
from . models import Producto
# Create your views here.

def index(request):
    return render(request, 'Tienda/index.html',)

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Tienda/lista_productos.html', {
        # 'producto': lista_productos[0:2],
        'productos': productos,
    })

def detail(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    return render(request, 'Tienda/detail.html',  {
        'nombre': producto.nombre,
        'precio': producto.precio,
    })
