from django.test import TestCase
from Apps.Biblioteca.models import Genero
from Apps.usuarios.models import MyUser
# Create your tests here.

class TestPruebas(TestCase):
    def setUp(self):
        Genero.objects.create(id=1,nombre='Genero1',activo=True)
        Genero.objects.create(id=2,nombre='Genero2',activo=True)

    def test_genero_creado(self):
        exists=Genero.objects.filter(nombre='Genero1').exists()
        exists2=Genero.objects.filter(id=2).exists()
        self.assertEqual(exists, True)
        self.assertEqual(exists2, True)

class TestPruebas2(TestCase):
    def setUp(self):
        MyUser.objects.create(id=1,username='jose',email='josematias@hotmail.es',
        is_superuser=False,is_staff=False,is_active=True)
        MyUser.objects.create(id=2,username='diego',email='diego@hotmail.es',
        is_superuser=True,is_staff=True,is_active=True)

    def test_usuario_activo(self):
        exists=MyUser.objects.filter(id=2,is_active=True).exists()
        exists2=MyUser.objects.filter(id=1,is_active=True).exists()
        self.assertEqual(exists, True)
        self.assertEqual(exists2, True)

class TestPruebas3(TestCase):
    def setUp(self):
        MyUser.objects.create(id=1,username='jose',email='josematias@hotmail.es',
        is_superuser=False,is_staff=False,is_active=True)

    def test_usuario_eliminar(self):
        user=MyUser.objects.get(id=1)
        user.delete()
        exists=MyUser.objects.filter(id=1,is_active=True).exists()
        self.assertEqual(exists, False)
