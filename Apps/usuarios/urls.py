from django.urls import path
from .views import baseAdmin

app_name='Mantenedores'
urlpatterns = [
    path('',baseAdmin,name='administracion'),
]
