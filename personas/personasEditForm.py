from django import forms
from .models import Persona  

class PersonaEdicionForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
        }