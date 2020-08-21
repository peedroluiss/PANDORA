from django.shortcuts import render, redirect
from django.http import HttpRequest

from Models.Establecimiento.FormsE import FormsEstablecimiento
from Models.Establecimiento.models import Establecimiento


class FormularioEstablecimientoView(HttpRequest):

    def  index(request):
        establecimiento = FormsEstablecimiento()
        return render(request,'EstablecimientoIndex.html',{'form':establecimiento})

    def  procesar_formulario(request):
        establecimiento = FormsEstablecimiento(request.POST)
        if establecimiento.is_valid():
            establecimiento.save()
            establecimiento= FormsEstablecimiento()
        return render(request,'EstablecimientoIndex.html', {'form': establecimiento, "mensaje": "Ok"})

    def listar_establecimientos(request):
        establecimientos = Establecimiento.objects.all()
        return render(request, "ListaEstablecimientos.html", {"establecimientos": establecimientos})


    def modificarE(request, id):
        MODDE = Establecimiento.objects.get(id_esta=id)
        data = {
            'form': FormsEstablecimiento(instance=MODDE)
        }
        if request.method == 'POST':
            formulario = FormsEstablecimiento(data=request.POST, instance=MODDE)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'ModificarEstablecimiento.html', data)


    def eliminarE(request, id):
        Establecimiento.objects.filter(id_esta=id).delete()
        return redirect(to="listarEstablecimientos")
