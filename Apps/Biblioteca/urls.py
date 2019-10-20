from django.urls import path
from .views import crearAutor,cargarLibro,listarAutor,editarAutor,eliminarAutor

urlpatterns=[
    path('crear_autor/', crearAutor,name='crear_autor'),
    path('listar_autor/', listarAutor,name='listar_autor'),
    path('Libro/',cargarLibro,name='libro'),
    path('editar_autor/<int:id>/', editarAutor,name='editar_autor'),
    path('eliminar_autor/<int:id>/', eliminarAutor,name='eliminar_autor'),
]