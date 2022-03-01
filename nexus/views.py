from django.http import HttpResponse
from django.shortcuts import render
from productos.models import Producto


def base(request):

    return render(request, 'base.html')



def index(request):

    return render(request, 'index.html')



def productos(request):
    producto = Producto.objects.all().order_by('codigo')
    contexto = {'lista_productos':producto}
    return render(request, 'productos.html', contexto)



def resultado_busqueda(request):
    if request.GET["elemento_buscado"]:
        productos_buscados = request.GET["elemento_buscado"]
        lista_encontrados = Producto.objects.filter(nombre__icontains=productos_buscados)

        contexto = {'encontrados':lista_encontrados, 'query':productos_buscados}

        return render(request, 'resultado_busqueda.html', contexto)
    else:
        return render(request, 'sin_resultados.html')