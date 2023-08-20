from django.urls import path, include
from SitioWeb import views

urlpatterns = [
    path('login/',  views.login, name='login'),
    #path('singin/', views.persona_Carga, name='singin'), (esto lleva a la carga de persona)
]