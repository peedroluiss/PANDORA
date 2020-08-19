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

from Models.Departamento.views import FormularioDepartamentoView
from Models.Director.views import FormularioDirectorView
from Models.Establecimiento.views import FormularioEstablecimientoView
from Models.Municipio.views import FormularioMunicipioView
from Views.HomeView import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),

    #RUTAS DEPARTAMENTO
    path('registrarDepartamento/', FormularioDepartamentoView.index, name = 'registrarDepartamento'),
    path('guardarDepartamento/', FormularioDepartamentoView.procesar_formulario, name = 'guardarDepartamento'),
    path('listarDepartamento/', FormularioDepartamentoView.listar_departamentos, name = 'listarDepartamento'),
    path("editarDepartamentos/<id>", FormularioDepartamentoView.modificarD, name="MODIFICARD"),
    path("listarDepartamento/<id>", FormularioDepartamentoView.eliminarD, name="ELIMINARD"),

    #RUTAS DIRECTOR
    path('registrarDirector/', FormularioDirectorView.index, name = 'registrarDirector'),
    path('guardarDirector/', FormularioDirectorView.procesar_formulario, name = 'guardarDirector'),
    path('listarDirectores/', FormularioDirectorView.listar_directores, name='listarDirectores'),
    path("editarDirectores/<id>", FormularioDirectorView.modificarDi, name="MODIFICARDI"),
    path("listarDirectores/<id>", FormularioDirectorView.eliminarDi, name="ELIMINARDI"),

    #RUTAS MUNICIPIO
    path('registrarMuncipio/', FormularioMunicipioView.index, name = 'registrarMunicipio'),
    path('guardarMunicipio/', FormularioMunicipioView.procesar_formulario, name = 'guardarMunicipio'),
    path('listarMunicipios/', FormularioMunicipioView.listar_municipios, name='listarMunicipios'),
    path("editarMunicipios/<id>", FormularioMunicipioView.modificarM, name="MODIFICARM"),
    path("listarMunicipios/<id>", FormularioMunicipioView.eliminarM, name="ELIMINARM"),

    #RUTAS ESTABLECIMIENTO
    path('registrarEstablecimiento/', FormularioEstablecimientoView.index, name='registrarEstablecimiento'),
    path('guardarEstablecimiento/', FormularioEstablecimientoView.procesar_formulario, name='guardarEstablecimiento'),
    path('listarEstablecimientos/', FormularioEstablecimientoView.listar_establecimientos, name='listarEstablecimientos'),
    path("editarEstablecimientos/<id>", FormularioEstablecimientoView.modificarE, name="MODIFICARE"),
    path("listarEstablecimientos/<id>", FormularioEstablecimientoView.eliminarE, name="ELIMINARE"),

]
