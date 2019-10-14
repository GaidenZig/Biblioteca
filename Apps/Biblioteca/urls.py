from django.urls import path
from .views import crearAutor,cargarLibro

app_name='Biblioteca'
urlpatterns=[
    path('crear_autor/', crearAutor,name='crear_autor'),
    path('Libro/<pk>',cargarLibro,name='libro')
]
