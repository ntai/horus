from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from ..models import Current
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CurrentSerializer,
    CurrentLocationSerializer
)
from meta.models import Location, ValueType
from django.shortcuts import get_object_or_404

class CurrentModelAPIViewSet(ModelViewSet):
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        l = Location.objects.get(slug=self.kwargs.get('location'))
        vt = ValueType.objects.get(slug=self.kwargs.get('value_type'))
        return get_object_or_404(Current, location_id=l.id, value_type_id=vt.id)
    pass


class CurrentLocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = CurrentLocationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pass
