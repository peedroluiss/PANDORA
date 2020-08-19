from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from Models.Departamento.FormsD import FormularioDepartamento
from Models.Departamento.models import Departamento


class FormularioDepartamentoView(HttpRequest):

    def index(request):
        departamento = FormularioDepartamento()
        return render(request,"DepartamentoIndex.html",{"form": departamento})

    def procesar_formulario(request):
        departamento = FormularioDepartamento(request.POST)
        if departamento.is_valid():
            departamento.save()
            departamento = FormularioDepartamento()
        return render(request,"DepartamentoIndex.html",{"form": departamento, "mensaje": 'ok'})

    def listar_departamentos(request):
        departamentos = Departamento.objects.all()
        return render(request,"ListaDepartamentos.html", {"departamentos":departamentos})

    def modificarD(request, id):
        MODD = Departamento.objects.get(id_depa=id)
        data = {
            'form': FormularioDepartamento(instance=MODD)
        }
        if request.method == 'POST':
            formulario = FormularioDepartamento(data=request.POST, instance=MODD)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'ModificarDepartamento.html', data)

    def eliminarD(request, id):
        Departamento.objects.filter(id_depa=id).delete()
        return redirect(to="listarDepartamento")
