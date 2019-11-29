from Apps.Biblioteca.models import Editorial,Genero
from rest_framework import serializers

class EditorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Editorial
        fields=['nombre']

class GeneroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields=['nombre','activo']
