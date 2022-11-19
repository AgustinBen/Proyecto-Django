from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import date
from . models import Producto
# Create your views here.


# producto_queso = {
#     'nombre' : 'Queso reggianito',
#     'precio' : '800.0',
#     'marca' : 'Paladini',
#     'imagen' : 'Tienda/img/reggianito.png',
#     'slug' : 'paladini-reggianito',
# }
# producto_salamin= {
#     'nombre' : 'Salamin',
#     'precio' : '299.9',
#     'marca' : 'Paladini',
#     'imagen' : 'Tienda/img/salamin.png',
#     'slug' : 'paladini-salamin',
# }
# producto_manteca = {
#     'nombre' : 'Manteca',
#     'precio' : '150.0',
#     'marca' : 'La Serenisima',
#     'imagen' : 'Tienda/img/manteca.png',
#     'slug' : 'serenisima-manteca',
# }

# lista_productos = [
#     producto_queso,
#     producto_salamin,
#     producto_manteca,
# ]


def index(request):
    return render(request, 'Tienda/index.html',)

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Tienda/lista_productos.html', {
        # 'producto': lista_productos[0:2],
        'productos': productos,
    })

def product_detail(request, slug):
    return render(request, 'Tienda/product-detail')


# def productos_index (request, item):
#     pass
