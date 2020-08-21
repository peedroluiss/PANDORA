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
from Models.Alumno.views import FormularioAlumnoView
from Models.Catedratico.views import FormularioCatedraticoView
from Models.Seccion.views import FormularioSeccionView
from Models.Departamento.views import FormularioDepartamentoView
from Models.Director.views import FormularioDirectorView
from Models.Establecimiento.views import FormularioEstablecimientoView
from Models.Municipio.views import FormularioMunicipioView
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

# URL DE ALUMNOS - MYNORB
     path("registrarAlumno/", FormularioAlumnoView.index, name='registrarAlumno'),
     path("guardarAlumno/", FormularioAlumnoView.procesar_formulario, name='guardarAlumno'),
     path("listarAlumnos/", FormularioAlumnoView.listar_alumnos, name='listarAlumnos'),
     path("listarAlumnos/<id>",FormularioAlumnoView.eliminarAlumno, name="ELIMINARALUMNO"),
     path("editarAlumnos/<id>",FormularioAlumnoView.modificarAlumno, name="MODIFICARALUMNO"),

# URL DE CATEDRATICOS - MYNORB
     path("registrarCatedratico/", FormularioCatedraticoView.index, name='registrarCatedratico'),
     path("guardarCatedratico/", FormularioCatedraticoView.procesar_formulario_catedratico, name='guardarCatedratico'),
     path("listarCatedraticos/", FormularioCatedraticoView.listar_Catedraticos, name='listarCatedraticos'),
     path("listarCatedraticos/<id>",FormularioCatedraticoView.eliminarCatedratico, name="ELIMINARCATEDRATICO"),
     path("editarCatedraticos/<id>",FormularioCatedraticoView.modificarCatedratico, name="MODIFICARCATEDRATICO"),

# URL DE SECCION - MYNORB
     path("registrarSeccion/", FormularioSeccionView.index, name='registrarSeccion'),
     path("guardarSeccion/", FormularioSeccionView.procesar_formulario_seccion, name='guardarSeccion'),
     path("listarSeccions/", FormularioSeccionView.listar_Seccions, name='listarSeccions'),
     path("listarSeccions/<id>",FormularioSeccionView.eliminarSeccion, name="ELIMINARSECCION"),
     path("editarSeccions/<id>",FormularioSeccionView.modificarSeccion, name="MODIFICARSECCION"),

    # RUTAS DEPARTAMENTO - WILSON
    path('registrarDepartamento/', FormularioDepartamentoView.index, name='registrarDepartamento'),
    path('guardarDepartamento/', FormularioDepartamentoView.procesar_formulario, name='guardarDepartamento'),
    path('listarDepartamento/', FormularioDepartamentoView.listar_departamentos, name='listarDepartamento'),
    path("editarDepartamentos/<id>", FormularioDepartamentoView.modificarD, name="MODIFICARD"),
    path("listarDepartamento/<id>", FormularioDepartamentoView.eliminarD, name="ELIMINARD"),

    # RUTAS DIRECTOR - WILSON
    path('registrarDirector/', FormularioDirectorView.index, name='registrarDirector'),
    path('guardarDirector/', FormularioDirectorView.procesar_formulario, name='guardarDirector'),
    path('listarDirectores/', FormularioDirectorView.listar_directores, name='listarDirectores'),
    path("editarDirectores/<id>", FormularioDirectorView.modificarDi, name="MODIFICARDI"),
    path("listarDirectores/<id>", FormularioDirectorView.eliminarDi, name="ELIMINARDI"),

    # RUTAS MUNICIPIO - WILSON
    path('registrarMuncipio/', FormularioMunicipioView.index, name='registrarMunicipio'),
    path('guardarMunicipio/', FormularioMunicipioView.procesar_formulario, name='guardarMunicipio'),
    path('listarMunicipios/', FormularioMunicipioView.listar_municipios, name='listarMunicipios'),
    path("editarMunicipios/<id>", FormularioMunicipioView.modificarM, name="MODIFICARM"),
    path("listarMunicipios/<id>", FormularioMunicipioView.eliminarM, name="ELIMINARM"),

    # RUTAS ESTABLECIMIENTO -WILSON
    path('registrarEstablecimiento/', FormularioEstablecimientoView.index, name='registrarEstablecimiento'),
    path('guardarEstablecimiento/', FormularioEstablecimientoView.procesar_formulario, name='guardarEstablecimiento'),
    path('listarEstablecimientos/', FormularioEstablecimientoView.listar_establecimientos, name='listarEstablecimientos'),
    path("editarEstablecimientos/<id>", FormularioEstablecimientoView.modificarE, name="MODIFICARE"),
    path("listarEstablecimientos/<id>", FormularioEstablecimientoView.eliminarE, name="ELIMINARE"),
]

