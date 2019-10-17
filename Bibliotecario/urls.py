"""Bibliotecario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps.Biblioteca.views import Home ,galeria,perfil,libro,crearAutor
from Apps.usuarios.views import register, Login_view, logout_view 
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Biblioteca/', include(('Apps.Biblioteca.urls','Biblioteca'))),
    path('', Home, name='index'),   
    path('register/',register, name='registro'),
    path('login/',Login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('galeria/',galeria, name='galeria'),
    path('perfil/',perfil, name='perfil'),
    path('libro/',libro, name='libro'),
    path('crearAutor/',crearAutor, name='crearAutor'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
