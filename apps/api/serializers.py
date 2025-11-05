from rest_framework import serializers
from apps.ordenes.models import OrdenDetalle, Platillo

class PlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platillo
        fields = ['nombre']

class OrdenDetalleSerializer(serializers.ModelSerializer):
    
    platillo = PlatilloSerializer(read_only=True)
    
    class Meta:
        model = OrdenDetalle
        fields = ['platillo', 'cantidad', 'notas']