from django import forms
from .models import Autor,Genero

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields=['primer_nombre','apellido','nacimiento','muerte']
        

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields=['nombre','activo']