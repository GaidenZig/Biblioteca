from django.urls import path
from .views import crearAutor, editarAutor, eliminarAutor, listarAutor
from .views import crearGenero, editarGenero, eliminarGenero, listarGenero
from .views import crearEditorial,editarEditorial,eliminarEditorial,listarEditorial
from .views import cargarLibro

app_name='Biblio'
urlpatterns=[
    path('Libro/<pk>',cargarLibro,name='libro'),

    path('editar_autor/<int:id>/', editarAutor,name='editar_autor'),
    path('eliminar_autor/<int:id>/', eliminarAutor,name='eliminar_autor'),
    path('crear_autor/', crearAutor,name='crear_autor'),
    path('listar_autor/', listarAutor,name='listar_autor'),
    
    path('editar_genero/<int:id>/', editarGenero,name='editar_genero'),
    path('eliminar_genero/<int:id>/', eliminarGenero,name='eliminar_genero'),
    path('crear_genero/', crearGenero,name='crear_genero'),
    path('listar_genero/', listarGenero,name='listar_genero'),

    path('editar_editorial/<int:id>/', editarEditorial,name='editar_editorial'),
    path('eliminar_editorial/<int:id>/', eliminarEditorial,name='eliminar_editorial'),
    path('crear_editorial/', crearEditorial,name='crear_editorial'),
    path('listar_editorial/', listarEditorial,name='listar_editorial'),
]
