from django.db import models
from Apps.usuarios.models import MyUser

# Create your models here.
class Autor(models.Model):
    id= models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    nacimiento = models.DateField(blank=True, null=False)
    muerte = models.DateField('Fallecimiento', null=True, blank=True)
    descripcion= models.TextField(null=True, blank=True, max_length=2000, help_text="bibliografía corta del autor")

    def __str__(self):
        return '%s, %s' % (self.apellido, self.primer_nombre)

class Genero(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")
    activo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre=models.CharField(unique=True,max_length=80)

class Libro(models.Model):
    titulo=models.CharField('Titulo', max_length=100)
    portada=models.ImageField(upload_to='images/', default='images/no-book-image.jpg')
    resumen=models.TextField(max_length=2000, help_text="Ingrese el resumen del libro")
    editorial=models.ForeignKey(Editorial,on_delete=models.SET_NULL, blank=True, null=True)
    autor=models.ManyToManyField(Autor,help_text="selecciones un autor")
    isbn=models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genero = models.ManyToManyField(Genero, help_text="Seleccione un genero")
    fech_salida=models.DateField('Fecha de publicación', null=True, blank=True)
    estrellas=models.FloatField()
    paginas=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class InstanciaLibro(models.Model):
    fech_inicio=models.DateField('Fecha de entrega', null=False, blank=False)
    fech_vencimiento=models.DateField('Fecha de devolución', null=False, blank=False)
    libro=models.ForeignKey(Libro, on_delete=models.SET_NULL, blank=True, null=True)
    usuario=models.ForeignKey(MyUser, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return 'libro: {}, usuario: {}'.format(self.libro.titulo,self.usuario.username)

class Puntuacion(models.Model):
    valor=models.FloatField(null=True, blank=True)
    fecha=models.DateTimeField(auto_now=True, null=True, blank=True)
    usuario=models.ForeignKey(MyUser, on_delete=models.SET_NULL, blank=True, null=True)
    libro=models.ForeignKey(Libro, on_delete=models.SET_NULL, blank=True, null=True)



    