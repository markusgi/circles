from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from circles.serializers import CircleSerializer
from circles.models import Circle



# List all persons: api/circles/list/
class ListCirclesAPIView(ListAPIView):
    serializer_class = CircleSerializer
    queryset = Circle.objects.all()
    permission_classes = []

class RetrieveUpdateDestroyCircleAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CircleSerializer
    queryset = Circle.objects.all()
    permission_classes = []
    lookup_field = 'id'
