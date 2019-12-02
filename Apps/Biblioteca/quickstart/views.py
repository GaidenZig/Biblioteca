from Apps.Biblioteca.models import Editorial ,Genero
from rest_framework import viewsets
from Apps.Biblioteca.quickstart.serializers import EditorialSerializer, GeneroSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows editorials to be viewed or edited.
    """
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class GenresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genres to be viewed or edited.
    """
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
