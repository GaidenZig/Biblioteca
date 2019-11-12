from django import forms
from .models import Autor,Genero, Libro,Editorial,Slider

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields=['primer_nombre','apellido','nacimiento','muerte']
        widgets={
            'primer_nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el Nombre del Autor'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el Apellido del Autor'
                }
            ),
            'nacimiento':forms.SelectDateWidget(
                attrs={
                    'class':'form-control-date'                    
                }
            ),
            'muerte':forms.SelectDateWidget(
                attrs={
                    'class':'form-control-date'                    
                }
            )
        }
        
class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields=['nombre']

class SliderForm(forms.ModelForm):
    class Meta:
        model=Slider
        fields = "__all__"

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields=['nombre','activo']


class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=['titulo','portada','resumen','editorial','autor','isbn','genero','activo','copias','fech_salida','estrellas','paginas']
    
