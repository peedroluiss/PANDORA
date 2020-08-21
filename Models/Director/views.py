from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from Models.Departamento.FormsD import FormularioDepartamento
from Models.Departamento.models import Departamento
from Models.Director.FormsDi import FormularioDirector
from Models.Director.models import Director


class FormularioDirectorView(HttpRequest):

    def index(request):
        director = FormularioDirector()
        return render(request,"DirectorIndex.html",{"form": director})

    def procesar_formulario(request):
        director = FormularioDirector(request.POST)
        if director.is_valid():
            director.save()
            director = FormularioDirector()
        return render(request,"DirectorIndex.html",{"form": director, "mensaje": 'ok'})

    def listar_directores(request):
        directores = Director.objects.all()
        return render(request,"ListaDirectores.html", {"directores":directores})

    def modificarDi(request, id):
        MODDI = Director.objects.get(id_direct=id)
        data = {
            'form': FormularioDirector(instance=MODDI)
        }
        if request.method == 'POST':
            formulario = FormularioDirector(data=request.POST, instance=MODDI)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'ModificarDirector.html', data)

    def eliminarDi(request, id):
        Director.objects.filter(id_direct=id).delete()
        return redirect(to="listarDirectores")