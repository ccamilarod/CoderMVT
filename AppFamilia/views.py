from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Familia
from django.template import Template, Context, loader
# Create your views here.


def familia(request):
    f1 = Familia(nombre = "Mirta", edad = 60, birth = "15/08")
    f1.save()
    f2 = Familia(nombre = "Sergio", edad = 55, birth = "14/08")
    f2.save()
    f3 = Familia(nombre = "Julieta", edad = 32, birth = "2/05")
    f3.save()

    diccionario = {
        "nombre1":f1.nombre, "edad1":f1.edad, "cumpleanios1":f1.birth,
        "nombre2":f2.nombre, "edad2":f2.edad, "cumpleanios2":f2.birth,
        "nombre3":f3.nombre, "edad3":f3.edad, "cumpleanios3":f3.birth,
        }

    plantilla = loader.get_template("templateApp.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)



    

    