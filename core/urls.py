from django.urls import path

from core.views import PersonListAPIView, CarsListAPIView, PersonUpdateAPIView, PersonDestroyAPIView

urlpatterns = [
    path("patients/", PersonListAPIView.as_view(), name="patients"),
    path("cars/", CarsListAPIView.as_view(), name="cars"),
    path("patients/<int:pk>", PersonUpdateAPIView.as_view(), name="patients"),
    path("patientsdelete/<int:pk>", PersonDestroyAPIView.as_view(), name="patientsdelete")

]