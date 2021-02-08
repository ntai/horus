from rest_framework.viewsets import ModelViewSet
from ..models import History
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    HistorySerializer,
)


class HistoryModelAPIViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return self.queryset.get(current=self.kwargs.get('id'))
    pass

