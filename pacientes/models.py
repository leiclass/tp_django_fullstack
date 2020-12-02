from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    dni = models.CharField(unique=True, max_length=8, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return f"{self.dni}: {self.nombre} {self.apellido}"

# Create your models here.
class Historia(models.Model):
    consulta = models.CharField(max_length=100)
    fecha = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha}: {self.paciente} - {self.medico}  {self.consulta}"

