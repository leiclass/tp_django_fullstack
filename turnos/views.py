from django.shortcuts import render
from .models import Turno
from pacientes.models import Paciente
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'turnos.html', {
        'turnos': Turno.objects.all()
    })

def reservar(request):
    mensaje = ''
    if request.method == 'POST':
        fecha = request.POST['fecha']
        paciente_id = int(request.POST['paciente'])
        paciente = Paciente.objects.get(id=paciente_id)
        medico_id = int(request.POST['medico'])
        medico = User.objects.get(id=medico_id)

        t = Turno(fecha=fecha, paciente=paciente, medico=medico)
        t.save()
        return HttpResponseRedirect(reverse('turnos:index'))
            
    
    return render(request, 'reservar.html', {
        'pacientes' : Paciente.objects.all(),
        'medicos' : Group.objects.get(name="medicos").user_set.all(), 
        'mensaje' : mensaje
    })

def turno(request, turno_id):
    un_turno = Turno.objects.get(id=turno_id)
    return render(request, 'turno.html', {
        'turno' : un_turno
    })