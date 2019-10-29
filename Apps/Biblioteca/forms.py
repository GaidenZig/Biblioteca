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
                    'class':'libro-control',
                    'placeholder':'Ingrese titulo del libro'
                }
            ),
            'portada':forms.FileInput(
                attrs={
                    'class':'libro-control',
                    'accept':'image/'
                }
            ),
            'resumen':forms.TextInput(
                attrs={
                    'class':'libro-control',
                    'placeholder':'Una breve descripcion del libro'
                }
            ),
            'editorial':forms.Select(
                attrs={
                    'class':'libro-control'                    
                }
            ),
            'autor':forms.SelectMultiple(
                attrs={
                    'class':'libro-control'                    
                }
            ),
            'isbn':forms.TextInput(
                attrs={
                    'class':'libro-control',
                    'placeholder':'Isbn del libro (13 dígitos)'
                }
            ),
            'genero':forms.SelectMultiple(
                attrs={
                    'class':'libro-control'                    
                }
            ),
            'fech_salida':forms.SelectDateWidget(
                attrs={
                    'class':'libro-control-date'                    
                }
            ),
            'estrellas':forms.NumberInput(
                attrs={
                    'class':'libro-control'
                }
            ),
            'paginas':forms.NumberInput(
                attrs={
                    'class':'libro-control'
                }
            )
        }

