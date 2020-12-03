from django.urls import path
from . import views

app_name = 'pacientes'
urlpatterns = [
    path("", views.index, name="index"),
    path("ver/<id>", views.ver, name="ver")
]