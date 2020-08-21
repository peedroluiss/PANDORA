from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Catedratico.FormsCatedratico import FormularioCatedratico
from Models.Catedratico.models import Catedratico


class FormularioCatedraticoView(HttpRequest):

        #METODOS PARA REGISTRAR
    def index(request):
        Catedratico= FormularioCatedratico()
        return render(request, "CatedraticoIndex.html", {"form":Catedratico })

    def procesar_formulario_catedratico(request):
        Catedratico = FormularioCatedratico(request.POST)
        if Catedratico.is_valid():
            Catedratico.save()
            Catedratico = FormularioCatedratico()
        return render(request, "CatedraticoIndex.html", {"form":Catedratico, "mensaje":'OK'})

        #METODOS PARA VISUALIZAR
    def listar_Catedraticos(request):
        Catedraticos = Catedratico.objects.all()
        return render(request, "ListaCatedraticos.html",{"lb_Catedraticos": Catedraticos})


        #METODO PARA ELIMINAR
    def eliminarCatedratico(request,id):
                Catedratico.objects.filter(id_catedra=id).delete()
                return redirect(to="listarCatedraticos")

        #METODO PARA EDITAR
    def modificarCatedratico(request, id):
            MOD= Catedratico.objects.get(id_catedra=id)
            data = {
                'form': FormularioCatedratico(instance=MOD)
            }
            if request.method == 'POST':
                formulario = FormularioCatedratico(data=request.POST, instance=MOD)
                if formulario.is_valid():
                    formulario.save()
                    data['mensaje'] = "Se ha actualizado el registro."
                    data['form'] = formulario
            return render(request, 'Modificar_catedratico.html', data)