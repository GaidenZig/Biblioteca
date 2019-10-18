from django.urls import path
from .views import cargarLibro

app_name='Biblioteca'
urlpatterns=[   
    path('Libro/<pk>',cargarLibro,name='libro'),
]
