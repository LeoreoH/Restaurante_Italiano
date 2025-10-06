import django.forms as forms
from apps.ordenes.models import Mesa, MesaEstado

class MesaEstadoForm(forms.ModelForm):
    class Meta:
        model = MesaEstado
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del estado'}),
        }

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['nombre', 'capacidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mesa'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Capacidad de la mesa'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
