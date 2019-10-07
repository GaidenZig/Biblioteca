from django.shortcuts import render,redirect
from .forms import AutorForm
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from Apps.usuarios.models import MyUser

# Create your views here.
def Home(request):    
    current_user=request.user   
    return render(request,'index.html',{'user':current_user})
    
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

