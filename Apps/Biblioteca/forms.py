from django import forms
from .models import Autor,Genero, Libro,Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields=['primer_nombre','apellido','nacimiento','muerte']
        
class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields=['nombre']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields=['nombre','activo']


class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=['titulo','portada','resumen','editorial','autor','isbn','genero','activo','copias','fech_salida','estrellas','paginas']
    
