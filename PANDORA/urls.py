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
from Views.HomeView import HomeView
from Models.Alumno.views import FormularioAlumnoView
from Models.Catedratico.views import FormularioCatedraticoView
from Models.Seccion.views import FormularioSeccionView


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),

# URL DE ALUMNOS
     path("registrarAlumno/", FormularioAlumnoView.index, name='registrarAlumno'),
     path("guardarAlumno/", FormularioAlumnoView.procesar_formulario, name='guardarAlumno'),
     path("listarAlumnos/", FormularioAlumnoView.listar_alumnos, name='listarAlumnos'),
     path("listarAlumnos/<id>",FormularioAlumnoView.eliminarAlumno, name="ELIMINARALUMNO"),
     path("editarAlumnos/<id>",FormularioAlumnoView.modificarAlumno, name="MODIFICARALUMNO"),

# URL DE CATEDRATICOS
     path("registrarCatedratico/", FormularioCatedraticoView.index, name='registrarCatedratico'),
     path("guardarCatedratico/", FormularioCatedraticoView.procesar_formulario_catedratico, name='guardarCatedratico'),
     path("listarCatedraticos/", FormularioCatedraticoView.listar_Catedraticos, name='listarCatedraticos'),
     path("listarCatedraticos/<id>",FormularioCatedraticoView.eliminarCatedratico, name="ELIMINARCATEDRATICO"),
     path("editarCatedraticos/<id>",FormularioCatedraticoView.modificarCatedratico, name="MODIFICARCATEDRATICO"),

# URL DE SECCION
     path("registrarSeccion/", FormularioSeccionView.index, name='registrarSeccion'),
     path("guardarSeccion/", FormularioSeccionView.procesar_formulario_seccion, name='guardarSeccion'),
     path("listarSeccions/", FormularioSeccionView.listar_Seccions, name='listarSeccions'),
     path("listarSeccions/<id>",FormularioSeccionView.eliminarSeccion, name="ELIMINARSECCION"),
     path("editarSeccions/<id>",FormularioSeccionView.modificarSeccion, name="MODIFICARSECCION"),

]
