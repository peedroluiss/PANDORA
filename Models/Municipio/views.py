from django.shortcuts import render, redirect
from django.http import HttpRequest


from Models.Municipio.FormsM import FormsMunicipio
from Models.Municipio.models import Municipio


class FormularioMunicipioView(HttpRequest):

    def  index(request):
        municipio = FormsMunicipio()
        return render(request,'MunicipioIndex.html',{'form':municipio})

    def  procesar_formulario(request):
        municipio = FormsMunicipio(request.POST)
        if municipio.is_valid():
            municipio.save()
            municipio= FormsMunicipio()
        return render(request,'MunicipioIndex.html', {'form': municipio, "mensaje": "Ok"})

    def listar_municipios(request):
        municipios = Municipio.objects.all()
        return render(request, "ListaMunicipios.html", {"municipios": municipios})


    def modificarM(request, id):
        MODM = Municipio.objects.get(id_muni=id)
        data = {
            'form': FormsMunicipio(instance=MODM)
        }
        if request.method == 'POST':
            formulario = FormsMunicipio(data=request.POST, instance=MODM)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'ModificarMunicipio.html', data)


    def eliminarM(request, id):
        Municipio.objects.filter(id_muni=id).delete()
        return redirect(to="listarMunicipios")

