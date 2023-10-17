from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from viajes.models import Viaje_General, Destino
from .serializers import ViajeGeneralSerializer
from django.contrib.auth.models import User
from django.db.models import Q

def filtrar_viajes_queryset(viajes, destino, dias_hasta, calif):
    if destino:
        viajes = viajes.filter(viaje_dia__destinos__icontains=destino).distinct()

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
          
        viajes = Viaje_General.objects.all().filter(esPrivado=False)
        viajes = self.get_queryset().filter(estado='ACTIVO')
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
          
        # Obtener todos los viajes desde la base de datos
        viajes = Viaje_General.objects.all().filter(usuario=user_obj.pk)
        viajes= filtrar_viajes_queryset(viajes,destino,dias_hasta,calif)

        serializer = self.get_serializer(viajes.order_by('-calificacion'), many=True)
      
        return Response(serializer.data)