from rest_framework import serializers
from .models import Pokemon

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'type',]