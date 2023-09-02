from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from viajes.models import Viaje_General, Destino
from .serializers import ViajeGeneralSerializer

"""def api_viajes(request): #Api para mostrar los viajes que hay cargados
    viajes = Viaje_General.objects.order_by('nombreViaje')
    return render(request, 'api_viajes.html', {'lista_viajes':viajes})"""

class ViajeGeneralViewSet(viewsets.ModelViewSet):
    serializer_class = ViajeGeneralSerializer
    queryset = Viaje_General.objects.all()
     
    # Definición de la vista para que muestre TODOS los viajes
    @action(detail=False)  # Decorador para una acción que no requiere un objeto específico
    def todos_los_viajes(self, request):
        # Obtiene todos los viajes desde la base de datos
        viajes = self.get_queryset()

        serializer = self.get_serializer(viajes, many=True)
        return Response(serializer.data)
    
     #filtrar por destino y rango de días
    @action(detail=False, methods=['GET'])
    def filtrar_viajes(self, request):
        destino = request.GET.get('destino')
        dias_desde = request.GET.get('dias-desde')
        dias_hasta = request.GET.get('dias-hasta')

        # Obtener todos los viajes desde la base de datos
        viajes = self.get_queryset()

        # Aplicar filtro por destino si se proporciona
        if destino:
            viajes = viajes.filter(viaje_dia__destinos__nombre__icontains=destino)

        # Aplicar filtro por rango de días si se proporciona
        if dias_desde and dias_hasta:
            viajes = viajes.filter(cantidadDias__gte=dias_desde, cantidadDias__lte=dias_hasta)
        elif dias_desde:
            viajes = viajes.filter(cantidadDias__gte=dias_desde)
        elif dias_hasta:
            viajes = viajes.filter(cantidadDias__lte=dias_hasta)

        
        serializer = self.get_serializer(viajes, many=True)
        return Response(serializer.data)

