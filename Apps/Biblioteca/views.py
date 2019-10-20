from django.shortcuts import render,redirect
from .forms import AutorForm
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from sjango.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from Apps.usuarios.models import MyUser
from .models import Genero, Libro,Autor

# Create your views here.
def Home(request):   
    queryset=request.GET.get("Buscar") 
    current_user=request.user   
    top_libros=Libro.objects.filter(puntuacion__gt=4)
    if queryset:
        libros=Libro.objects.filter(Q(titulo__icontains=queryset))
        return render(request,'Biblioteca/galeria.html',{'libros':libros})
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
    return render(request,'Biblioteca/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores=Autor.objects.all()
    return render(request,'Biblioteca/listar_autor.html',{'autores':autores})

def editarAutor(request,id):
    autor_form=None
    error=None
    try:
        autor=Autor.objects.get(id = id)
        if request.method =='GET':
            autor_form=AutorForm(instance = autor)
        else:
            autor_form=AutorForm(request.POST,instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('listar_autor')
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Biblioteca/editar_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor=Autor.objects.get(id=id)
    autor.delete()
    return redirect('Biblioteca:listar_autor')
   
def cargarLibro(request):
    print(request.GET) 

def galeria(request):
    queryset=request.GET.get("Buscar")
    libros=Libro.objects.all() 
    if queryset:
        libros=Libro.objects.filter(Q(titulo__icontains=queryset))
    paginate_by=3
    return render(request,'Biblioteca/galeria.html',{'libros':libros})

def perfil(request):    
    current_user=request.user 
    return render(request,'Accounts/perfil.html',{'user':current_user})

def libro(request): 
    return render(request,'Biblioteca/Libro.html',{})

