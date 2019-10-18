from django.shortcuts import render,redirect
from Apps.usuarios.models import MyUser
from .models import Genero, Libro, Autor, Editorial

# Create your views here.
#documentación para las queries: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.all

def Home(request):    
    current_user=request.user   
    top_libros=Libro.objects.filter(estrellas__gt=4)
    return render(request,'index.html',{'user':current_user,'top':top_libros})
    
def cargarLibro(request,pk):    
    libro=Libro.objects.get(id__exact=pk)
    autores=libro.autor.all()
    editorial=libro.editorial
    return render(request,'Biblioteca/Libro.html',{'libro':libro,'autores':autores,'editorial':editorial})



