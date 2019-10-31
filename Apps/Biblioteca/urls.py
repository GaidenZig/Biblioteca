from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import crearAutor, editarAutor, eliminarAutor, listarAutor
from .views import crearGenero, editarGenero, eliminarGenero, listarGenero
from .views import crearLibro, editarLibro, eliminarLibro, listarLibro, cargarLibro

app_name='Biblio'
urlpatterns=[
    path('libro/<pk>',cargarLibro,name='libro'),

    path('editar_libro/<int:pk>',login_required(editarLibro.as_view()),name='editar_libro'),
    path('eliminar_libro/<int:pk>',login_required(eliminarLibro.as_view()),name='eliminar_libro'),
    path('crear_libro/',login_required(crearLibro.as_view()),name='crear_libro'),
    path('libro/', login_required(listarLibro.as_view()), name='listar_libro'),

    path('editar_autor/<int:id>/', editarAutor,name='editar_autor'),
    path('eliminar_autor/<int:id>/', eliminarAutor,name='eliminar_autor'),
    path('crear_autor/', crearAutor,name='crear_autor'),
    path('listar_autor/', listarAutor,name='listar_autor'),
    
    path('editar_genero/<int:id>/', editarGenero,name='editar_genero'),
    path('eliminar_genero/<int:id>/', eliminarGenero,name='eliminar_genero'),
    path('crear_genero/', crearGenero,name='crear_genero'),
    path('listar_genero/', listarGenero,name='listar_genero'),
]
