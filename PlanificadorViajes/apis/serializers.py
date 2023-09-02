from rest_framework import serializers
from viajes.models import Viaje_General

class ViajeGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje_General
        fields = '__all__'