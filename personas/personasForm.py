from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-3'}),max_length=30,required=True)
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-3'}),max_length=30,required=True)
    cedula = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-3'}),max_length=30,required=True)
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-3'}),max_length=30,required=True)
