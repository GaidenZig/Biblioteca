from django.urls import path
from .views import crearAutor,cargarLibro,listarAutor,editarGenero,eliminarGenero,editarAutor,eliminarAutor,adminBase

urlpatterns=[
    path('editar_autor/<int:id>/', editarAutor,name='editar_autor'),
    path('eliminar_autor/<int:id>/', eliminarAutor,name='eliminar_autor'),
    path('editar_genero/<int:id>/', editarGenero,name='editar_genero'),
    path('eliminar_genero/<int:id>/', eliminarGenero,name='eliminar_genero'),
]