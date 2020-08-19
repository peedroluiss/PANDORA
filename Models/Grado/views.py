from django.shortcuts import render

from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models import Grado
from Models.Grado.FormsGra import FormularioGrado
from Models.Grado.models import Grado

class FormularioGradoView(HttpRequest):

    # METODOS PARA REGISTRAR
    def indexg(request):
        grado = FormularioGrado()
        return render(request, "GradoIndex.html", {"form": grado})

    def procesar_formulariog(request):
        grado = FormularioGrado(request.POST)
        if grado.is_valid():
            grado.save()
            grado = FormularioGrado()
        return render(request, "GradoIndex.html", {"form": grado, "mensaje": 'OK'})

    # METODOS PARA VISUALIZAR
    def listar_grado(request):
            grados = Grado.objects.all()
            return render(request, "ListaGrado.html", {"lb_grados": grados})
 # METODO PARA EDITAR
    def modificarGrado(request, id):
        MOD = Grado.objects.get(id_grado=id)
        data = {
            'form': FormularioGrado(instance=MOD)
        }
        if request.method == 'POST':
            formulario = FormularioGrado(data=request.POST, instance=MOD)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'ModificarGrado.html', data)

        # METODO PARA ELIMINAR
    def eliminarGrado(request, id):
            Grado.objects.filter(id_grado=id).delete()
            return redirect(to="listarGrados")