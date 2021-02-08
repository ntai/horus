# Models
from ..models import Location, ValueType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class LocationSerializer(ModelSerializer):
    slug = serializers.SlugField(max_length=100)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Location
        exclude = ['id']
        lookup_field = 'slug'
        pass
    pass

class ValueTypeSerializer(ModelSerializer):
    slug = serializers.SlugField(max_length=100)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = ValueType
        exclude = ['id']
        lookup_field = 'slug'
        pass
    pass

