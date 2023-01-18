from rest_framework import serializers
from restfull_api.models import Person, Species

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name' ,'birth_year', 'eye_color', 'specied')

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id', 'name', 'classification', 'language')
