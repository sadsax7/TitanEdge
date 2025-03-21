from django.shortcuts import render, HttpResponse
#importamos el modelo del servicio

# Create your views here.

def home(request):
    
    return render(request, "TitanCorpApp/home.html")


def tienda(request):

    return render(request, "TitanCorpApp/tienda.html")


def blog(request):

    return render(request, "TitanCorpApp/blog.html")


def contacto(request):

    return render(request, "TitanCorpApp/contacto.html")