from django.conf import settings
from django.db import models
from pacientes import models as pacientes_models
from django.utils import timezone

# Create your models here.
class Turno(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    paciente = models.ForeignKey(pacientes_models.Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    asistio = models.BooleanField(null=True)

    def __str__(self):
        return f"Turno: {self.fecha} -- Paciente: {self.paciente}, Médico: {self.medico}"

