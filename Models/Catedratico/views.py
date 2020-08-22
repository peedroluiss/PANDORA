from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa

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

    def listar_Catedraticos2(request):
        Catedraticos = Catedratico.objects.all()
        return render(request, "Reportes_catedraticos.html",{"lb_Catedraticos": Catedraticos})


    def Reportpdfcatedratico(self, *args, **kwargs):
        template = get_template('ReporteCatedratico.html')
        context = {'report': Catedratico.objects.all(),
                   'comp': {'name': 'Reporte de Catedraticos'}
                   }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Catedraticos.pdf"'
        pisaStatus = pisa.CreatePDF(

            html, dest=response)

        if pisaStatus.err:
            return HttpResponse('we had some errors <pre>' + html + '</pre>')

        return response