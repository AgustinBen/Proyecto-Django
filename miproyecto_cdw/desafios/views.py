from django.shortcuts import render
from django.http import HttpResponse, Http404
# from django.template.loader import render_to_string

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
    'diciembre': False,
}

def index(request):
    # return HttpResponse('hola mundo!')
    pagina = ''
    # for mes in meses.keys():
    #     pagina += '<a href= %s ><h1>%s</h1></a>'%(mes, mes)
    # return HttpResponse(pagina)
    return render(request, "desafios/index.html", {
        'meses': meses.keys(),
    })
    




def monthly_challenge(request, month):
    pagina = '<h1>%s</h1>'%(month)
    for mes in meses.keys():
        if month == mes:
            # pagina += '<p>%s</p>'%(meses[mes])
            # texto_desafio = render_to_string(“desafios/desafio.html”)
            # return HttpResponse(pagina)
            return render(request, "desafios/desafios.html", {
                'month': month,
                'texto': meses[mes],
            })
    raise Http404()   # return HttpResponse('<h1>No se encontro el mes</h1>')