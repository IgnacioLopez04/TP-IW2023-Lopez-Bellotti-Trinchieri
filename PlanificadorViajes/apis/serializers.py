from rest_framework import serializers
from viajes.models import Viaje_General, Viaje_Dia

class ViajeGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje_General
        fields = '__all__'
class DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje_Dia
        fields = '__all__'