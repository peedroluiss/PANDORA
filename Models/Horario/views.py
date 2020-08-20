from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models import Horario
from Models.Horario.FormsG import FormularioHorario
from Models.Horario.models import Horario

class FormularioHorarioView(HttpRequest):


    #METODOS PARA REGISTRAR
    def indexh(request):
        horario = FormularioHorario()
        return render(request, "HorarioIndex.html", {"form": horario})

    def procesar_formularioh(request):
        horario = FormularioHorario(request.POST)
        if horario.is_valid():
            horario.save()
            horario = FormularioHorario()
        return render(request, "HorarioIndex.html", {"form": horario,"mensaje": 'OK'})

    #METODOS PARA VISUALIZAR
    def listar_horario(request):
        horarios = Horario.objects.all()
        return render(request, "ListaHorario.html",{"lb_horarios": horarios})

    #METODO PARA EDITAR
    def modificarH(request, id):
            MOD = Horario.objects.get(id_hora=id)
            data = {
                'form': FormularioHorario(instance=MOD)
            }
            if request.method == 'POST':
                formulario = FormularioHorario(data=request.POST, instance=MOD)
                if formulario.is_valid():
                    formulario.save()
                    data['mensaje'] = "Se ha actualizado el registro."
                    data['form'] = formulario
            return render(request, 'ModificarHorario.html', data)

     # METODO PARA ELIMINAR
    def eliminarH(request, id):
        Horario.objects.filter(id_hora=id).delete()
        return redirect(to="listarHorarios")

