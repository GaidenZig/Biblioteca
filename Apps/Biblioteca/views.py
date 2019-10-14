from django.shortcuts import render,redirect
from .forms import AutorForm
from django.template import RequestContext
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from Apps.usuarios.models import MyUser
from .models import Genero, Libro, Autor, Editorial

# Create your views here.
#documentación para las queries: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.all

def Home(request):    
    current_user={'nombre':'hola'}   
    top_libros=Libro.objects.filter(estrellas__gt=4)
    return render(request,'index.html',{'user':current_user,'top':top_libros})
    
def crearAutor(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')       
    else:
        autor_form=AutorForm()
    return render(request,'Biblioteca/crear_autor.html')

def cargarLibro(request,pk):    
    libro=Libro.objects.get(id__exact=pk)
    autores=libro.autor.all()
    editorial=libro.editorial
    return render(request,'Biblioteca/Libro.html',{'libro':libro,'autores':autores,'editorial':editorial})


