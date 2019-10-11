from django.urls import path
from .views import crearAutor,cargarLibro

urlpatterns=[
    path('crear_autor/', crearAutor,name='crear_autor'),
    path('Libro/',cargarLibro,name='libro')
]