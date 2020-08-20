"""PANDORA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.Calendario.views import FormularioCalendarioView
from Models.Grado.views import FormularioGradoView
from Models.Horario.views import FormularioHorarioView
from Models.Programa.views import FormularioProgramaView
from Views.HomeView import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    #GESTION GRADOS -KENNEDY-
    path("registrarHorario/", FormularioHorarioView.indexh, name='registrarHorario'),
    path("guardarHorario/", FormularioHorarioView.procesar_formularioh, name='guardarHorario'),
    path("listarHorarios/", FormularioHorarioView.listar_horario, name='listarHorarios'),
    path("editarHorarios/<id>",FormularioHorarioView.modificarH, name="modificarHorarios"),
    path("listarHorarios/<id>",FormularioHorarioView.eliminarH, name="eliminarHorarios"),

    #GESTION CALENDARIO -KENNEDY-
    path("registrarCalendario/", FormularioCalendarioView.indexcale, name='registrarCalendario'),
    path("guardarCalendario/", FormularioCalendarioView.procesar_formulariocale, name='guardarCalendario'),
    path("listarCalendarios/", FormularioCalendarioView.listar_calendario, name='listarCalendarios'),
    path("editarCalendarios/<id>",FormularioCalendarioView.modificarCale, name="modificarCalendarios"),
    path("listarCalendarios/<id>", FormularioCalendarioView.eliminarCale, name="eliminarCalendarios"),

    #GESTION PROGRAMA DE CURSOS -KENNEDY-
    path("registrarPrograma/", FormularioProgramaView.indexp, name='registrarPrograma'),
    path("guardarPrograma/", FormularioProgramaView.procesar_formulariop, name='guardarPrograma'),
    path("listarProgramas/", FormularioProgramaView.listar_programa, name='listarProgramas'),
    path("editarProgramas/<id>", FormularioProgramaView.modificarP, name="modificarProgramas"),
    path("listarProgramas/<id>", FormularioProgramaView.eliminarP, name="eliminarProgramas"),

    #GESTION GRADOS -KENNEDY-
    path("registrarGrado/", FormularioGradoView.indexg, name='registrarGrado'),
    path("guardarGrado/", FormularioGradoView.procesar_formulariog, name='guardarGrado'),
    path("listarGrados/", FormularioGradoView.listar_grado, name='listarGrados'),
    path("editarGrados/<id>", FormularioGradoView.modificarGrado, name="modificarGrados"),
    path("listarGrados/<id>", FormularioGradoView.eliminarGrado, name="eliminarGrados"),
]

