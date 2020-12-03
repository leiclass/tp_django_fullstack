from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Paciente, Historia
from .forms import HistoriaPacienteForm

# Create your views here.
def index(request):
    data = {
        'pacientes': Paciente.objects.all()
    }
    return render(request, 'pacientes.html', data)

# Create your views here.
def ver(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('usuarios:login'))
   
    if request.method == 'POST':
        formulario = HistoriaPacienteForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form']  = formulario

    paciente = get_object_or_404(Paciente, id=id)
    historia = Historia.objects.filter(paciente=paciente)
    data = {
        'paciente': paciente,
        'historia': historia,
        'form': HistoriaPacienteForm(initial={'paciente': paciente, 'medico': request.user})
    }
    return render(request, 'paciente.html', data)
