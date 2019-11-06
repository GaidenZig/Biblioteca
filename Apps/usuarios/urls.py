from django.urls import path
from .views import adminBase,editarUsuario,eliminarUsuario,crearUsuarior, listarUsuario
app_name='Mantenedores'
urlpatterns = [
    path('',adminBase,name='administracion'),

    path('crear_usuario/', crearUsuarior,name='crear_usuario'),
    path('editar_usuarios/<int:id>/', editarUsuario,name='editar_usuarios'),
    path('eliminar_usuarios/<int:id>/', eliminarUsuario,name='eliminar_usuarios'),
    path('listar_usuarios/', listarUsuario,name='listar_usuarios'),   

]
