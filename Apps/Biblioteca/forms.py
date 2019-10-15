from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields=['primer_nombre','apellido','nacimiento','muerte']

class LibroCreationForm(forms.ModelForm):
    class Meta:
        model=Libro
        widgets={}

