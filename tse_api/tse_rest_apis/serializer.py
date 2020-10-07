from rest_framework import serializers
from tse_rest_apis.models import Symbol

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ['name']
