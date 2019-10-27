from django.urls import path
from .views import editarUsuario,eliminarUsuario,crearUsuarior

urlpatterns=[

    path('eliminar_usuarios/<int:id>/', eliminarUsuario,name='eliminar_usuarios'),
    path('editar_usuarios/<int:id>/', editarUsuario,name='editar_usuarios'),
    
 
]