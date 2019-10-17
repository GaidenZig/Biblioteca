from django.urls import path
from .views import crearAutor,cargarLibro,listarAutor

urlpatterns=[
    path('crear_autor/', crearAutor,name='crear_autor'),
    path('listar_autor/', listarAutor,name='listar_autor'),
    path('Libro/',cargarLibro,name='libro')
]