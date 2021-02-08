# Models
from ..models import History
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class HistorySerializer(ModelSerializer):
    location = serializers.SlugField(max_length=200)
    value_type = serializers.SlugField(max_length=200)
    value = serializers.CharField(max_length=200)
    timestamp = serializers.DateTimeField()

    class Meta:
        model = History
        lookup_field = 'location'
        pass
    pass

