from django import forms
from django.contrib.auth.models import User
from .models import Paciente, Historia

class HistoriaPacienteForm(forms.ModelForm):

    paciente = forms.ModelChoiceField( 
        queryset=Paciente.objects.all(),
        widget=forms.HiddenInput(attrs={'readonly': 'readonly'})
    )
    medico = forms.ModelChoiceField( 
        queryset=User.objects.all(),
        widget=forms.HiddenInput(attrs={'readonly': 'readonly'})
    )
    

    class Meta: 
        model = Historia
        fields = '__all__'
