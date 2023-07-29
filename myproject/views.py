from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo!!!")

def bienvenida(request):
    return HttpResponse("<html><h1>Bienvenidos a Django con Python</h1></html>")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    respuestaDia = f"Hoy es: <br> {dia}"
    return HttpResponse(respuestaDia)

def saludoPersonal(request, nombre):
    
    saludo = f"Bienvenido {nombre}" #creamos variable
    return HttpResponse(saludo)



def pruebaTemplate(request):
    with open("C:/Users/Trufa/Documents/Python/Clase 17/myproject/myproject/plantillas/index.html") as file:
        plantilla = Template(file.read())
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
