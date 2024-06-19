from django.urls import path

from core.views import PersonListAPIView, CarsListAPIView

urlpatterns = [
    path("patients/", PersonListAPIView.as_view(), name="patients"),
    path("cars/", CarsListAPIView.as_view(), name="cars")

]