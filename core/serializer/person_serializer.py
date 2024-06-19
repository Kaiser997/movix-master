from rest_framework import serializers
from core.models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['primer_nombre', 'primer_apellido',
        'segundo_nombre', 'segundo_apellido',
        'identificacion', 'tipo_identificacion',
        'correo','celular']

