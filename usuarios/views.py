from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('usuarios:login'))
    
    group_secretaria = Group.objects.get(name="secretaria").user_set.all()
    group_medicos = Group.objects.get(name="medicos").user_set.all()

    if request.user in group_secretaria:
        return render(request, 'index-secretaria.html')
    elif request.user in group_medicos:
        return render(request, 'index-medicos.html')
    else:
        return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('usuarios:index'))
        else:
            return render(request, 'login.html', {
                "mensaje" : "Credenciales NO válidas"
            })
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {
        'mensaje' : 'Usted se ha desconectado exitosamente'
    })