from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Persona
from django.urls import reverse

class PersonaTests(APITestCase):
    def setUp(self):
        self.patient=Persona.objects.create(
            primer_nombre = 'elkin',
            primer_apellido = 'prada',
            segundo_nombre = 'daniel',
            segundo_apellido = 'gomez',
            identificacion = '454654564',
            tipo_identificacion = "CC",
            correo = "elkin@gmail.com",
            celular ="324535465"
        )


    def test_create_persona(self):
        url = reverse("patients")
        data = { 
            "primer_nombre" : "roger",
            "primer_apellido" : "rubio",
            "segundo_nombre" : "andres",
            "segundo_apellido" : "mosquera",
            "identificacion" : "1013673129",
            "tipo_identificacion" : "CC",
            "correo" : "roger@gmail.com",
            "celular" : "3654654"
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Persona.objects.filter(identificacion ="454654564").count(), 1)
            
    def test_update_persona(self):
        
        url = reverse('patients', kwargs={'pk': self.patient.pk})  
        data = { 
            "primer_nombre" : "Roger"
        }    

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Persona.objects.get().primer_nombre, "Roger")

    def test_delete_persona(self):
        
        url = reverse('patientsdelete', kwargs={'pk': self.patient.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        


# Create your tests here.
