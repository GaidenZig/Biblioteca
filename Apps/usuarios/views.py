from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,get_user_model,logout
from .forms import UserCreationForm,UserLoginForm

# Create your views here.
def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    context={
        'form':form
    }
    return render(request,"Accounts/register.html",context)

def Login_view(request, *args, **kwargs):
    form= UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request,user_obj)
        return HttpResponseRedirect("")
    return render(request,'Accounts/login.html',{"form":form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")



