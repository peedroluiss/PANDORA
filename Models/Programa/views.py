from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models import Programa
from Models.Programa.FormsP import FormularioPrograma
from Models.Programa.models import Programa

class FormularioProgramaView(HttpRequest):

    # METODOS PARA REGISTRAR
    def indexp(request):
        programa = FormularioPrograma()
        return render(request, "ProgramaIndex.html", {"form": programa})

    def procesar_formulariop(request):
        programa = FormularioPrograma(request.POST)
        if programa.is_valid():
           programa.save()
           programa = FormularioPrograma()
        return render(request, "ProgramaIndex.html", {"form": programa, "mensaje": 'OK'})

    # METODOS PARA VISUALIZAR
    def listar_programa(request):
            programas = Programa.objects.all()
            return render(request, "ListaPrograma.html", {"lb_programas": programas})

 # METODO PARA EDITAR
    def modificarP(request, id):
        MOD = Programa.objects.get(id_prog=id)
        data = {
            'form': FormularioPrograma(instance=MOD)
        }
        if request.method == 'POST':
            formulario = FormularioPrograma(data=request.POST, instance=MOD)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'ModificarPrograma.html', data)

# METODO PARA ELIMINAR
    def eliminarP(request, id):
            Programa.objects.filter(id_prog=id).delete()
            return redirect(to="listarProgramas")