from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'viaje_general', views.ViajeGeneralViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('todos_los_viajes/', views.ViajeGeneralViewSet.as_view({'get': 'todos_los_viajes'}), name='todos_los_viaj0es'),
     path('filtrar_viajes/', views.ViajeGeneralViewSet.as_view({'get': 'filtrar_viajes'}), name='filtrar_viajes'),
     path('viajes_usuario/', views.ViajeGeneralViewSet.as_view({'get': 'viajes_usuario'}), name='viajes_usuario'),
     path('un_viaje/', views.ViajeGeneralViewSet.as_view({'get': 'buscar_un_viaje'}), name='buscar_un_viaje')
]
    