from django.shortcuts import render,redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView

from .models import Genero, Libro, Autor, Editorial
from .forms import AutorForm, GeneroForm,LibroForm,EditorialForm
from Apps.usuarios.models import MyUser

# Create your views here.
#documentación para las queries: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.all

# Create your views here.
def Home(request):   
    current_user=request.user   
    top_libros=Libro.objects.filter(estrellas__gt=4)
    print(top_libros)
    return render(request,'index.html',{'user':current_user,'top':top_libros})


def cargarLibro(request,pk):    
    libro=Libro.objects.get(id__exact=pk)
    autores=libro.autor.all()
    editorial=libro.editorial
    return render(request,'Biblioteca/Libro.html',{'libro':libro,'autores':autores,'editorial':editorial})

def galeria(request):
    queryset=request.GET.get("Buscar")
    libros=Libro.objects.all() 
    if queryset:
        libros=Libro.objects.filter(Q(titulo__icontains=queryset))
    paginator=Paginator(libros,1)
    page=request.GET.get('page')
    libros=paginator.get_page(page)
    return render(request,'Biblioteca/galeria.html',{'libros':libros})

def perfil(request):    
    current_user=request.user 
    return render(request,'Accounts/perfil.html',{'user':current_user})

#(Mantenedores) Autor

def crearAutor(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('Biblio:listar_autor')       
    else:
        autor_form=AutorForm()
    return render(request,'Accounts/Admin/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores=Autor.objects.all()
    return render(request,'Accounts/Admin/listar_autor.html',{'autores':autores})

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
            return redirect('Biblio:listar_autor') 
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Accounts/Admin/editar_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor=Autor.objects.get(id=id)
    autor.delete()
    return redirect('Biblio:listar_autor') 
   

#(Mantenedores) Genero

def crearGenero(request):
    if request.method == 'POST':
        print(request.POST)
        genero_form = GeneroForm(request.POST)
        if genero_form.is_valid():
            genero_form.save()
            return redirect('Biblio:listar_genero')       
    else:
        genero_form=GeneroForm()
    return render(request,'Accounts/Admin/crear_genero.html',{'genero_form':genero_form})

def listarGenero(request):
    genero=Genero.objects.all()
    return render(request,'Accounts/Admin/listar_genero.html',{'genero':genero})

def editarGenero(request,id):
    genero_form=None
    error=None
    try:
        genero=Genero.objects.get(id = id)
        if request.method =='GET':
            genero_form=GeneroForm(instance = genero)
        else:
            genero_form=GeneroForm(request.POST,instance=genero)
            if genero_form.is_valid():
                genero_form.save()
            return redirect('Biblio:listar_genero')
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Accounts/Admin/editar_genero.html',{'genero_form':genero_form,'error':error})

def eliminarGenero(request,id):
    genero=Genero.objects.get(id=id)
    genero.delete()
    return redirect('Biblio:listar_genero')

#(Mantenedores) Libros
class ListadoLibros(ListView):
    model=Libro
    template_name= ''

class CrearLibro(CreateView):  
    model:Libro
    form_class:LibroForm


#(Mantenedores) Editorial

def crearEditorial(request):
    if request.method == 'POST':
        print(request.POST)
        editorial_form = EditorialForm(request.POST)
        if editorial_form.is_valid():
            editorial_form.save()
            return redirect('Biblio:listar_editorial')       
    else:
        editorial_form=EditorialForm()
    return render(request,'Accounts/Admin/crear_editorial.html',{'editorial_form':editorial_form})

def listarEditorial(request):
    editorial=Editorial.objects.all()
    return render(request,'Accounts/Admin/listar_editorial.html',{'editorial':editorial})

def editarEditorial(request,id):
    editorial_form=None
    error=None
    try:
        editorial=Editorial.objects.get(id = id)
        if request.method =='GET':
            editorial_form=EditorialForm(instance = editorial)
        else:
            editorial_form=EditorialForm(request.POST,instance=editorial)
            if editorial_form.is_valid():
                editorial_form.save()
            return redirect('Biblio:listar_editorial')
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Accounts/Admin/editar_editorial.html',{'editorial_form':editorial_form,'error':error})

def eliminarEditorial(request,id):
    editorial=Editorial.objects.get(id=id)
    editorial.delete()
    return redirect('Biblio:listar_editorial')