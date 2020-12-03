from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TurnoAltaForm
from .models import Turno
from pacientes.models import Paciente

# Create your views here.
def index(request):
    data = {
        'turnos': Turno.objects.all()
    }
    return render(request, 'turnos.html', data)

def reservar(request):    
    data = {
        'form': TurnoAltaForm()
    }
    if request.method == 'POST':
        formulario = TurnoAltaForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Turno reservado correctamente"
        else:
            data['form']  = formulario
    return render(request, 'reservar.html', data)

def modificar_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    data = {
        'form' : TurnoAltaForm(instance=turno)
    }
    if request.method == 'POST':
        formulario = TurnoAltaForm(data= request.POST, instance=turno)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect(reverse('turnos:index'))
            return redirect(to='turnos:index')

        #sino valida mando a editar con los datos del form
        data['form']  = formulario
    
    return render(request, 'editar-turno.html', data)

def eliminar_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    turno.delete()
    return redirect(to='turnos:index')