from django.urls import path
from . import views

app_name = 'turnos'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:turno_id>", views.turno, name="turno"),
    path("reservar/", views.reservar, name="reservar")
]