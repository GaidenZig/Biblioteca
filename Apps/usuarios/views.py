from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login,get_user_model,logout
from .forms import UserCreationForm,UserLoginForm,userForm
from Apps.Biblioteca.models import Autor,Libro
from django.core.exceptions import ObjectDoesNotExist
from .models import MyUser
from django.conf import settings
from django.core.mail import send_mail
from datetime import *


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
        return HttpResponseRedirect('/login_web')
       
    context={'form':form}
    return render(request,"Accounts/register.html",context)

def Login_view(request, *args, **kwargs):
    form= UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request,user_obj)        
        return HttpResponseRedirect("/")
    return render(request,'Accounts/login_web.html',{"form":form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

#Mantenedores de admin
def adminBase(request):    
    usuarios=MyUser.objects.filter(is_superuser=False).order_by('-id')
    return render(request,'Accounts/Admin/adminBase.html',{'usuarios':usuarios})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

#Mantenedores de admin
def adminBase(request):    
    current_user=request.user   
    return render(request,'Accounts/Admin/adminBase.html',{'user':current_user})


#(Mantenedores) Usuarios
def crearUsuarior(request):
    if request.method == 'POST':
        user_form = userForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return redirect('Mantenedores:listar_usuarios')    
    else:
        user_form=userForm()
    return render(request,'Accounts/Admin/crear_usuario.html',{'user_form':user_form})

def listarUsuario(request):
    usuarios=MyUser.objects.filter(is_active__exact=True)
    return render(request,'Accounts/Admin/listar_usuarios.html',{'usuarios':usuarios})

def editarUsuario(request,id):
    user_form=None
    error=None
    try:
        user=MyUser.objects.get(id = id)
        if request.method =='GET':
            user_form=userForm(instance = user)
        else:
            user_form=userForm(request.POST,request.FILES,instance=user)
            if user_form.is_valid():
                user_form.save()            
                return redirect('Mantenedores:listar_usuarios')
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Accounts/Admin/editar_usuarios.html',{'user_form':user_form,'error':error})

def eliminarUsuario(request,id):
    user=MyUser.objects.get(id=id)
    user.is_active=False
    user.save()
    return redirect('Mantenedores:listar_usuarios')



