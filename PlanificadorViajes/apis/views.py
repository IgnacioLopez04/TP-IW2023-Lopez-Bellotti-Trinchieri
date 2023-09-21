from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from viajes.models import Viaje_General, Destino
from .serializers import ViajeGeneralSerializer
from django.contrib.auth.models import User

"""def api_viajes(request): #Api para mostrar los viajes que hay cargados
    viajes = Viaje_General.objects.order_by('nombreViaje')
    return render(request, 'api_viajes.html', {'lista_viajes':viajes})"""

class ViajeGeneralViewSet(viewsets.ModelViewSet):
    serializer_class = ViajeGeneralSerializer
    queryset = Viaje_General.objects.all()
     
    # Definición de la vista para que muestre TODOS los viajes
    @action(detail=False)  # Decorador para una acción que no requiere un objeto específico
    def todos_los_viajes(self, request):
        # Obtiene todos los viajes desde la base de datos y los devuelve ordenados por calificacion
        viajes = self.get_queryset()

        serializer = self.get_serializer(viajes.order_by('-calificacion'), many=True)
        return Response(serializer.data)
    
     #filtrar por destino y rango de días, y devuelve ordenado por califación
    @action(detail=False, methods=['GET'])
    def filtrar_viajes(self, request):
        destino = request.GET.get('destino')
        dias_hasta = request.GET.get('dias-hasta')
        calif = request.GET.get('calificacion')
          
        # Obtener todos los viajes desde la base de datos
        viajes = self.get_queryset()

        # Aplicar filtro por destino si se proporciona
        if destino:
            viajes = viajes.filter(viaje_dia__destinos__nombre__icontains=destino).distinct()

        # Aplicar filtro por rango de días si se proporciona la cantidad de dias, para que busque al rededor de esa cantidad
        if dias_hasta:
            min_dias = max(0, int(dias_hasta) - 2) 
            max_dias = int(dias_hasta) + 2 
            viajes = viajes.filter(cantidadDias__range=(min_dias, max_dias))

        if calif:
            viajes = viajes.filter(calificacion__lte = calif)
            
        #devuelvo los viajes y ordeno de manera descendente los viajes por la calificación que tengan
        serializer = self.get_serializer(viajes.order_by('-calificacion'), many=True)
        return Response(serializer.data)

    @action(detail=False)
    def viajes_usuario(self, request):
        viajes = self.get_queryset()
        user = request.user.username
        user_obj = User.objects.get(username = user)
        serializer = self.get_serializer(viajes.filter(usuario=user_obj.pk).order_by('-calificacion'), many=True)
        return Response(serializer.data)
        
        
