from django import forms
from .models import Autor,Genero, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields=['primer_nombre','apellido','nacimiento','muerte']
        

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields=['nombre','activo']

class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=['titulo','portada','resumen','editorial','autor','isbn','genero','fech_salida','estrellas','paginas']
        label={
            'titulo':'Titulo del libro',
            'portada':'Imagen de portada',
            'resumen':'Descripcion breve del libro',
            'editorial':'Editorial del libro',
            'autor':'el autor',
            'isbn':'numero identificador unico del libro de 13 digitos',
            'genero':'generos del libro',
            'fech_salida':'fecha de publicacion del libro',
            'estrellas':'puntuacion(por defecto es 0)',
            'paginas':'numero de paginas del libro'
        }
        widgets={
            'titulo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese titulo del libro'
                }
            ),
            'portada':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'accept':'image/'
                }
            ),
            'resumen':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Una breve descripcion del libro'
                }
            ),
            'editorial':forms.Select(
                attrs={
                    'class':'form-control'                    
                }
            ),
            'autor':forms.SelectMultiple(
                attrs={
                    'class':'form-control'                    
                }
            ),
            'isbn':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Isbn del libro (13 dígitos)'
                }
            ),
            'genero':forms.SelectMultiple(
                attrs={
                    'class':'form-control'                    
                }
            ),
            'fech_salida':forms.SelectDateWidget(
                attrs={
                    'class':'form-control-date'                    
                }
            ),
            'estrellas':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'paginas':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            )
        }

