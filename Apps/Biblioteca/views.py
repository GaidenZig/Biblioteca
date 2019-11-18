from django.shortcuts import render,redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse


from .models import Genero, Libro, Autor, Editorial, Puntuacion, InstanciaLibro, Slider
from .forms import AutorForm, GeneroForm,LibroForm,EditorialForm, SliderForm
from Apps.usuarios.models import MyUser

# Create your views here.
#documentación para las queries: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.all

# Create your views here.
def Home(request):   
    current_user=request.user   
    slider=Slider.objects.all()
    top_libros=Libro.objects.filter(Q(estrellas__gt=4) & Q(activo__exact=True))        
    return render(request,'index.html',{'user':current_user,'top':top_libros,'slider':slider})


def cargarLibro(request,pk):    
    libro=Libro.objects.get(id__exact=pk)
    autores=libro.autor.all()
    editorial=libro.editorial   
    yaVoto=verificarVotacion(request.user,libro)
    return render(request,'Biblioteca/Libro.html',{'libro':libro,'autores':autores,'editorial':editorial,'yaVoto':yaVoto})

def galeria(request):
    queryset=request.GET.get("Buscar")
    libros=Libro.objects.filter(activo__exact=True) 
    if queryset:
        libros=Libro.objects.filter(Q(titulo__icontains=queryset) & Q(activo__exact=True))        
    paginator=Paginator(libros,1)
    page=request.GET.get('page')
    libros=paginator.get_page(page)
    return render(request,'Biblioteca/galeria.html',{'libros':libros})

def perfil(request):    
    current_user=request.user
    user=MyUser.objects.get(id__exact=current_user.id)
    dots=InstanciaLibro.objects.filter(usuario__id=user.id)
    result=dots.values('libro')
    lista=[]
    for obj in result:
        book=Libro.objects.get(id=obj['libro'])
        lista.append(book)        

    return render(request,'Accounts/perfil.html',{'user':current_user, 'reservas':lista})

def puntuacion(request):
    id=request.GET.get('id')
    libro=Libro.objects.get(id__exact=id)    
    return JsonResponse({'puntuacion':libro.estrellas})

def puntuar(request): 
    puntos=float(request.GET.get('puntos'))
    book=Libro.objects.get(id__exact=request.GET.get('idLibro'))
    user=MyUser.objects.get(id__exact=request.GET.get('idUsuario'))
    query=Puntuacion(valor=puntos, usuario=user, libro=book)
    if verificarVotacion(user,book)==False:
        valorEstrellas(book.id,puntos) 

    response = None
    if request.user.is_active and verificarVotacion(user,book)==False:
        query.save()               
        response=JsonResponse({})
    else:
        response=JsonResponse({"error":"usuario no autorizado para votar"})
        response.status_code=403

    return response

def valorEstrellas(libro,nuevoPuntaje):         
    promedio=0
    librito=Libro.objects.get(id=libro)
    objetos=Puntuacion.objects.filter(libro__id=libro)
    if not objetos:
        promedio=nuevoPuntaje
    else:
        suma=0 
        for objeto in objetos:
            suma += objeto.valor

        suma += nuevoPuntaje
        promedio= suma/objetos.count()

    print(promedio)
    librito.estrellas=promedio
    librito.save()

def verificarVotacion(usuario,libro):
    #Peligro inminente de eficiencia en el programa...    
    voto=False
    if usuario.is_active:        
        for objeto in Puntuacion.objects.all():
            if objeto.usuario.id == usuario.id and objeto.libro.id == libro.id:
                voto=True
    
    return voto

def reservar(request):
    libro=Libro.objects.get(id__exact=request.POST.get('idLibro'))
    usuario=MyUser.objects.get(id__exact=request.POST.get('idUsuario'))    
    fecha_inicio= request.POST.get('fechIni')
    fecha_vencimiento= request.POST.get('fechVenci')
    reserva=InstanciaLibro(fech_inicio=fecha_inicio,fech_vencimiento=fecha_vencimiento,libro=libro,usuario=usuario)    

    response=None
    if request.user.is_active:
        reserva.save()               
        response=JsonResponse({})
    else:
        response=JsonResponse({"error":"usuario no autorizado para votar"})
        response.status_code=403

    return response

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
class listarLibro(ListView):
    model= Libro
    template_name= 'Accounts/Admin/listar_libro.html'
    queryset=Libro.objects.filter(activo__exact= True)

class crearLibro(CreateView):  
    model= Libro
    form_class= LibroForm
    template_name= 'Accounts/Admin/crear_libro.html'
    success_url= reverse_lazy('Biblio:listar_libro')

class editarLibro(UpdateView):
    model= Libro
    form_class= LibroForm
    template_name= 'Accounts/Admin/editar_libro.html'
    success_url= reverse_lazy('Biblio:listar_libro')


class eliminarLibro(DeleteView):
    model= Libro    
    success_url= reverse_lazy('Biblio:listar_libro')
    def post(self, request,pk,*args,**kwargs):
        object=Libro.objects.get(id=pk)
        object.activo=False
        object.save()

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

def crearSlider(request):
    if request.method == 'POST':
        print(request.POST)
        slider_form = SliderForm(request.POST,request.FILES)
        slider=Slider.objects.all()
        if slider:
            return redirect('Biblio:listar_slider') 
        else:
            if slider_form.is_valid():
                slider_form.save()
                return redirect('Biblio:listar_slider')       
    else:
        slider_form=SliderForm()
    return render(request,'Accounts/Admin/crear_slider.html',{'slider_form':slider_form})

def listarSlider(request):
    slider=Slider.objects.all()
    return render(request,'Accounts/Admin/listar_slider.html',{'slider':slider})

def editarSlider(request,id):
    slider_form=None
    error=None
    try:
        slider=Slider.objects.get(id = id)
        if request.method =='GET':
            slider_form=SliderForm(instance = slider)
        else:
            slider_form=SliderForm(request.POST,request.FILES,instance=slider)
            if slider_form.is_valid():
                slider_form.save()
                return redirect('Biblio:listar_slider')
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Accounts/Admin/editar_slider.html',{'slider_form':slider_form,'error':error})
