from django.http import HttpRequest
from django.shortcuts import render, redirect
from Models.Alumno.FormsAlumno import FormularioAlumno
from Models.Alumno.models import Alumno


class FormularioAlumnoView(HttpRequest):

        #METODOS PARA REGISTRAR
    def index(request):
        alumno= FormularioAlumno()
        return render(request, "AlumnoIndex.html", {"form":alumno })

    def procesar_formulario(request):
        alumno = FormularioAlumno(request.POST)
        if alumno.is_valid():
            alumno.save()
            alumno = FormularioAlumno()
        return render(request, "AlumnoIndex.html", {"form":alumno, "mensaje":'OK'})

        #METODOS PARA VISUALIZAR
    def listar_alumnos(request):
        alumnos = Alumno.objects.all()
        return render(request, "ListaAlumnos.html",{"lb_alumnos": alumnos})


        #METODO PARA ELIMINAR
    def eliminarAlumno(request,id):
                Alumno.objects.filter(id_alumno=id).delete()
                return redirect(to="listarAlumnos")

        #METODO PARA EDITAR
    def modificarAlumno(request, id):
            MOD= Alumno.objects.get(id_alumno=id)
            data = {
                'form': FormularioAlumno(instance=MOD)
            }
            if request.method == 'POST':
                formulario = FormularioAlumno(data=request.POST, instance=MOD)
                if formulario.is_valid():
                    formulario.save()
                    data['mensaje'] = "Se ha actualizado el registro."
                    data['form'] = formulario
            return render(request, 'Modificar_alumno.html', data)