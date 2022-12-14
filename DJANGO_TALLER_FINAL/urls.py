"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django_seminario_app import views

urlpatterns = [
    path('', views.inicio),
    # crud
    path('listado/', views.listado_inscripciones),
    path('agregar_inscripcion/', views.crear_inscripcion),
    path('eliminar/<int:id>', views.eliminar_inscripcion),
    path('actualizar/<int:id>', views.actualizar_inscripcion),
    # class base view
    path('inscripciones_class/', views.ListaInscripciones.as_view()),
    path('inscripciones_class/<int:pk>', views.DetalleInscripcion.as_view()),
    # function base view
    path('instituciones_fun/', views.institucion_list),
    path('instituciones_fun/<int:id>', views.institucion_detalle),
    # api
    path('inscripciones_api/', views.inscripciones_api),

]
