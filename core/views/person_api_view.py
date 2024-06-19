
from rest_framework.views import APIView
from core.models import Persona
from rest_framework.response import Response
from core.serializer import PersonaSerializer
from rest_framework import generics

class PersonListAPIView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer   

class PersonUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


