from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models import Calendario
from Models.Calendario.FormsCale import FormularioCalendario
from Models.Calendario.models import Calendario

class FormularioCalendarioView(HttpRequest):

    # METODOS PARA REGISTRAR
    def indexcale(request):
        calendario = FormularioCalendario()
        return render(request, "CalendarioIndex.html", {"form": calendario})

    def procesar_formulariocale(request):
        horario = FormularioCalendario(request.POST)
        if horario.is_valid():
            horario.save()
            horario = FormularioCalendario()
        return render(request, "CalendarioIndex.html", {"form": horario, "mensaje": 'OK'})

        # METODOS PARA VISUALIZAR
    def listar_calendario(request):
            calendarios = Calendario.objects.all()
            return render(request, "ListaCalendario.html", {"lb_calendarios": calendarios})

         # METODO PARA EDITAR
    def modificarCale(request, id):
        MOD = Calendario.objects.get(id_ca=id)
        data = {
            'form': FormularioCalendario(instance=MOD)
        }
        if request.method == 'POST':
            formulario = FormularioCalendario(data=request.POST, instance=MOD)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'ModificarCalendario.html', data)

        # METODO PARA ELIMINAR
    def eliminarCale(request, id):
            Calendario.objects.filter(id_ca=id).delete()
            return redirect(to="listarCalendarios")
