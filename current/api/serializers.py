# Models
from meta.models import Location
from ..models import Current
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class CurrentSerializer(ModelSerializer):
    location = serializers.SlugField(max_length=32)
    value_type = serializers.SlugField(max_length=32)
    value = serializers.CharField(max_length=100)
    timestamp = serializers.DateTimeField()

    class Meta:
        model = Current
        lookup_field = ['location', 'value_type']
        fields = ['location', 'value_type', 'value', 'timestamp']
        pass
    pass

class CurrentLocationSerializer(ModelSerializer):
    slug = serializers.SlugField(max_length=32)

    class Meta:
        model = Location
        lookup_field = 'slug'
        fields = ['slug']
        pass
    pass

