from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

meses = {
    'enero': 'Practica Python',
    'febrero': 'Practica Python',
    'marzo': 'lee un libro',
    'abril': 'Practica Python',
    'mayo': 'Practica Python',
    'junio': 'lee dos libros',
    'julio': 'Practica Python',
    'agosto': 'Practica Python',
    'septiembre': 'lee tres libros',
    'octubre': 'Practica Python',
    'noviembre': 'Practica Python',
    'diciembre': 'lee cuatro libros',
}

def index(request):
    # return HttpResponse('hola mundo!')
    pagina = ''
    for mes in meses.keys():
        pagina += '<a href=%s><h1>%s</h1></a>'%(mes, mes)
    return HttpResponse(pagina)


def monthly_challenge(request, month):
    pagina = '<h1>%s</h1>'%(month)
    for mes in meses.keys():
        if month == mes:
            pagina += '<p>%s</p>'%(meses[mes])
            return HttpResponse(pagina)
    return HttpResponse('<h1>No se encontro el mes</h1>')