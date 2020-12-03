from django.urls import path
from . import views

app_name = 'turnos'
urlpatterns = [
    path("", views.index, name="index"),
    path("reservar/", views.reservar, name="reservar"),
    path("modificar/<id>/", views.modificar_turno, name="modificar_turno"),
    path("eliminar/<id>/", views.eliminar_turno, name="eliminar_turno")
]