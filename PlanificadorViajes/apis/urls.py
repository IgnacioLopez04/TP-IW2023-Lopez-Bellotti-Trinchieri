from django.urls import path
from . import views

urlpatterns = [
    path('viajes/', views.api_viajes, name='viajes'),
]
    