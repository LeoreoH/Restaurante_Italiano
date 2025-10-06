import django.forms as forms
from apps.platillos.models import Categoria, Platillo

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoria'}),
        }
        
class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ['nombre', 'descripcion', 'precio', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del platillo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del platillo'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del platillo'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
        