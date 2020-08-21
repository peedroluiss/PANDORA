from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Seccion.FormsSeccion import FormularioSeccion
from Models.Seccion.models import Seccion


class FormularioSeccionView(HttpRequest):

        #METODOS PARA REGISTRAR
    def index(request):
        Seccion= FormularioSeccion()
        return render(request, "SeccionIndex.html", {"form":Seccion })

    def procesar_formulario_seccion(request):
        Seccion = FormularioSeccion(request.POST)
        if Seccion.is_valid():
            Seccion.save()
            Seccion = FormularioSeccion()
        return render(request, "SeccionIndex.html", {"form":Seccion, "mensaje":'OK'})

        #METODOS PARA VISUALIZAR
    def listar_Seccions(request):
        Seccions = Seccion.objects.all()
        return render(request, "ListaSeccions.html",{"lb_Seccions": Seccions})


        #METODO PARA ELIMINAR
    def eliminarSeccion(request,id):
                Seccion.objects.filter(id_seccion=id).delete()
                return redirect(to="listarSeccions")

        #METODO PARA EDITAR
    def modificarSeccion(request, id):
            MOD= Seccion.objects.get(id_seccion=id)
            data = {
                'form': FormularioSeccion(instance=MOD)
            }
            if request.method == 'POST':
                formulario = FormularioSeccion(data=request.POST, instance=MOD)
                if formulario.is_valid():
                    formulario.save()
                    data['mensaje'] = "Se ha actualizado el registro."
                    data['form'] = formulario
            return render(request, 'Modificar_seccion.html', data)