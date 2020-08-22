from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa

from Models.Inscripcion.FormsInscripcion import FormularioInscripcion
from Models.Inscripcion.models import Inscripcion


class FormularioInscripcionView(HttpRequest):

        #METODOS PARA REGISTRAR
    def index(request):
        Inscripcion= FormularioInscripcion()
        return render(request, "InscripcionIndex.html", {"form":Inscripcion })

    def procesar_formulario_inscripcion(request):
        Inscripcion = FormularioInscripcion(request.POST)
        if Inscripcion.is_valid():
            Inscripcion.save()
            Inscripcion = FormularioInscripcion()
        return render(request, "InscripcionIndex.html", {"form":Inscripcion, "mensaje":'OK'})

        #METODOS PARA VISUALIZAR
    def listar_Inscripcions(request):
        Inscripcions = Inscripcion.objects.all()
        return render(request, "ListaInscripcion.html",{"lb_Inscripcions": Inscripcions})


        #METODO PARA ELIMINAR
    def eliminarInscripcion(request,id):
                Inscripcion.objects.filter(id_ins=id).delete()
                return redirect(to="listarInscripcions")

        #METODO PARA EDITAR
    def modificarInscripcion(request, id):
            MOD= Inscripcion.objects.get(id_ins=id)
            data = {
                'form': FormularioInscripcion(instance=MOD)
            }
            if request.method == 'POST':
                formulario = FormularioInscripcion(data=request.POST, instance=MOD)
                if formulario.is_valid():
                    formulario.save()
                    data['mensaje'] = "Se ha actualizado el registro."
                    data['form'] = formulario
            return render(request, 'Modificar_inscripcion.html', data)

    def ReportpdInscripcion(self, *args, **kwargs):
            template = get_template('Reporteinscripciones.html')
            context = {'report': Inscripcion.objects.all(),
                       'comp': {'name': 'Reporte de alumnos inscritos'}
                       }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Inscripciones.pdf"'
            pisaStatus = pisa.CreatePDF(

                html, dest=response)

            if pisaStatus.err:
                return HttpResponse('we had some errors <pre>' + html + '</pre>')

            return response