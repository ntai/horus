from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from ..models import Current
from .permissions import IsAuthenticated
from .serializers import (
    CurrentSerializer,
    CurrentLocationSerializer
)
from meta.models import Location, ValueType
import datetime
from rest_framework.response import Response

class CurrentModelAPIViewSet(ModelViewSet):
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        l = Location.objects.get(slug=self.kwargs.get('location'))
        vt = ValueType.objects.get(slug=self.kwargs.get('value_type'))
        object = Current.objects.filter(location_id=l.id, value_type_id=vt.id).first()
        if object is None:
            timestamp=datetime.datetime.now()
            object = Current(location = l, value_type=vt, value=-999, timestamp=timestamp)
            self.check_object_permissions(self.request, object)
            object.save()
            object = Current.objects.get(location_id=l.id, value_type_id=vt.id)
            pass
        # May raise a permission denied
        self.check_object_permissions(self.request, object)
        return object

    def list(self, request, *args, **kwargs):
        l = Location.objects.get(slug=self.kwargs.get('location'))
        queryset = self.filter_queryset(self.get_queryset().filter(location=l))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    pass


class CurrentLocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = CurrentLocationSerializer
    permission_classes = [IsAuthenticated]
    pass
