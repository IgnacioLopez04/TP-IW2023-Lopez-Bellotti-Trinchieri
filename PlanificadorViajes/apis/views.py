from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from viajes.models import Viaje_General
from .serializers import ViajeGeneralSerializer
from django.contrib.auth.models import User
from django.db.models import Q

def filtrar_viajes_queryset(viajes, destino, dias_hasta, calif):
    if destino:
        # Divide las palabras ingresadas por el usuario
        palabras = destino.split()
        # Inicializa un objeto Q vacío
        q_objects = Q()
        
        # Para cada palabra, agrega una condición al objeto Q
        for palabra in palabras:
            q_objects |= Q(viaje_dia__destinos__icontains=palabra)
        
        # Filtra los viajes usando el objeto Q final
        viajes = viajes.filter(q_objects).distinct()

    if dias_hasta:
        viajes = viajes.filter(cantidadDias__lte=dias_hasta)

    if calif:
        viajes = viajes.filter(calificacion__lte=calif)

    return viajes


class ViajeGeneralViewSet(viewsets.ModelViewSet):
    serializer_class = ViajeGeneralSerializer
    queryset = Viaje_General.objects.all()
     
    # Definición de la vista para que muestre TODOS los viajes
    @action(detail=False)  # Decorador para una acción que no requiere un objeto específico
    def todos_los_viajes(self, request):
        # Obtiene todos los viajes desde la base de datos y los devuelve ordenados por calificacion
        
        viajes = self.get_queryset().filter(estado='ACTIVO')
        viajes = viajes.filter(esPrivado=False)

        serializer = self.get_serializer(viajes.order_by('-calificacion'), many=True)
        return Response(serializer.data)
    
     #filtrar por destino y rango de días, y devuelve ordenado por califación
    @action(detail=False, methods=['GET'])
    def filtrar_viajes(self, request):
        destino = request.GET.get('destino')
        dias_hasta = request.GET.get('dias-hasta')
        calif = request.GET.get('calificacion')
          
        viajes = self.get_queryset().filter(esPrivado=False)
        viajes = viajes.filter(estado='ACTIVO')
        viajes= filtrar_viajes_queryset(viajes,destino,dias_hasta,calif)

        #devuelvo los viajes y ordeno de manera descendente los viajes por la calificación que tengan
        serializer = self.get_serializer(viajes.order_by('-calificacion'), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def viajes_usuario(self, request):
        user = request.user.username
        user_obj = User.objects.get(username = user)

        destino = request.GET.get('destino')
        dias_hasta = request.GET.get('dias-hasta')
        calif = request.GET.get('calificacion')
        estado= request.GET.get('estado')
          
        # Obtener todos los viajes desde la base de datos
        viajes = self.get_queryset().filter(usuario=user_obj.pk)
        viajes= filtrar_viajes_queryset(viajes,destino,dias_hasta,calif)

        if(estado == "no-terminado"):
            viajes = viajes.filter(estado="BORRADOR")
        elif(estado == "privado"):
            viajes = viajes.filter(esPrivado=True)

        serializer = self.get_serializer(viajes.order_by('-calificacion'), many=True)
      
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def buscar_un_viaje(self, request):
        id= request.GET.get('id')
        viaje = self.get_queryset().filter(id=id).first()
        serializer = self.get_serializer(viaje)

        return Response(serializer.data)
