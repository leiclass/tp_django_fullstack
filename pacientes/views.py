from django.shortcuts import render, get_object_or_404, redirect
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
   
    """ if request.method == 'POST':
        formulario = TurnoAltaForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Turno reservado correctamente"
        else:
            data['form']  = formulario """

    paciente = get_object_or_404(Paciente, id=id)
    historia = Historia.objects.filter(paciente=paciente)
    data = {
        'paciente': paciente,
        'historia': historia,
        'form': HistoriaPacienteForm()
    }
    return render(request, 'paciente.html', data)
