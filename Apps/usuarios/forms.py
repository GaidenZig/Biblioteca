from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.db.models import Q
from django import forms
from Apps.Biblioteca.models import Libro

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email',]

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user=super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct()

        if not user_qs_final.exists() and user_qs_final.count !=1:
            raise forms.ValidationError("invalid credentials - user does not exist")

        user_obj = user_qs_final.first()

        if not  user_obj.check_password(password):
            raise forms.ValidationError("credentials are not correct")

        self.cleaned_data["user_obj"]=user_obj

        return super(UserLoginForm, self).clean(*args, **kwargs)

#Mantenedores de admin
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