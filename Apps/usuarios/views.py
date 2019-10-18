from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,get_user_model,logout
from django.views.generic import CreateView,ListView
from .forms import UserCreationForm,UserLoginForm,LibroForm
from Apps.Biblioteca.models import Autor,Libro

# Create your views here.

"""
El HttpResponseRedirect, se tiene que modificar para cuando queramos agregar
alguna respuesta despues del 'registro','login' o 'logout'. Quiza la mejor manera
de 'avisar' sea esta de 'redireccionar' a algun url, creo yo...
(Diego Sandon)
"""
def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
       
    context={'form':form}
    return render(request,"Accounts/register.html",context)

def Login_view(request, *args, **kwargs):
    form= UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request,user_obj)        
        return HttpResponseRedirect("/")
    return render(request,'Accounts/login.html',{"form":form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

#Mantenedores de admin
def baseAdmin(request):
    return render(request,'Accounts/Admin/adminBase.html')

#(Mantenedores) Libros
class ListadoLibros(ListView):
    model=Libro
    template_name= ''

class CrearLibro(CreateView):  
    model:Libro
    form_class:LibroForm





