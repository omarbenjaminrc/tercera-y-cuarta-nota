
from django.shortcuts import render,redirect
# from django_seminario_app.models import Inscripcion
from django_seminario_app.forms import Form_inscripcion
from .serialiazers import InscripcionSerializer , InstitucionSerializer
from .models import Inscripcion, Institucion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404
from django.http import JsonResponse
# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def inscripciones_api(request):
    emple = Inscripcion.objects.all()
    data = {'Inscripciones' : list(emple.values('rut','nombre','telefono','fecha_inscripcion','hora','institucion','estado_reserva','observacion'))}
    return JsonResponse(data)


def index(request):
    return render(request, 'mostrar_inscripcion.html')

def listado_inscripciones(request):
    reserva = Inscripcion.objects.all()
    data = {'inscripciones': reserva}
    return render(request, 'mostrar_inscripcion.html', data)

def crear_inscripcion(request):
    form = Form_inscripcion()
    if request.method == 'POST':
        form = Form_inscripcion(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_inscripcion.html', data)

def eliminar_inscripcion(request,id):
    pro = Inscripcion.objects.get(id = id)
    pro.delete()
    return redirect('/')

def actualizar_inscripcion(request,id):
    pro = Inscripcion.objects.get(id = id)
    form = Form_inscripcion(instance=pro)
    if request.method == 'POST':
        form = Form_inscripcion(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'agregar_inscripcion.html',data)

# class base view

class ListaInscripciones(APIView):
    def get(self, request):
        inscripciones = Inscripcion.objects.all()
        serial = InscripcionSerializer(inscripciones, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscripcionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleInscripcion(APIView):
    def get_object(self, pk):
        try:
            return Inscripcion.objects.get(id=pk)
        except Inscripcion.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscripcion = self.get_object(pk)
        serial = InscripcionSerializer(inscripcion)
        return Response(serial.data)

    def put(self, request, pk):
        inscripcion = self.get_object(pk)
        serial = InscripcionSerializer(inscripcion, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscripcion = self.get_object(pk)
        inscripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# functio base view

@api_view(['GET','POST'])
def institucion_list (request):
    if request.method == 'GET':
        institucion = Institucion.objects.all()
        serial = InstitucionSerializer(institucion , many=True)
        return Response(serial.data)

    elif request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
def institucion_detalle(request,id):
    try:
        institucion = Institucion.objects.get(pk = id)
    except institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(institucion)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(institucion,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)