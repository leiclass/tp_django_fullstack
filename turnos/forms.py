from django import forms
from .models import Turno

class TurnoAltaForm(forms.ModelForm):

    class Meta: 
        model = Turno
        fields = ['fecha', 'paciente', 'medico']
        #fields = '__all__'