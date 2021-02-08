from rest_framework.viewsets import ModelViewSet
from ..models import Location, ValueType
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    LocationSerializer,
    ValueTypeSerializer,
)


class LocationModelAPIViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return self.queryset.get(locaion=self.kwargs.get('location'))
    pass


class ValueTypeModelAPIViewSet(ModelViewSet):
    queryset = ValueType.objects.all()
    serializer_class = ValueTypeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return self.queryset.get(locaion=self.kwargs.get('value_type'))
    pass

