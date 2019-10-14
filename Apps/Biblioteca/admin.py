from django.contrib import admin
from .models import Autor, Genero, Libro, InstanciaLibro, Editorial, Puntuacion

# Register your models here.
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(InstanciaLibro)
admin.site.register(Editorial)
admin.site.register(Puntuacion)

