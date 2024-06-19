from rest_framework import serializers
from core.models import Carro
from core.serializer import PersonaSerializer

class CarroSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()

    class Meta:
        model = Carro
        fields = ['marca', 'modelo',
        'placa', 'saldo', 'persona']