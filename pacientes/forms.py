from django import forms
from .models import Historia

class HistoriaPacienteForm(forms.ModelForm):

    class Meta: 
        model = Historia
        fields = ['consulta', 'fecha', 'medico']