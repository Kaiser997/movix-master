from rest_framework.views import APIView
from core.models import Carro
from rest_framework.response import Response
from core.serializer import CarroSerializer
from rest_framework import generics

class CarsListAPIView(generics.ListCreateAPIView):
    queryset = Carro.objects.all()    
    serializer_class = CarroSerializer


    