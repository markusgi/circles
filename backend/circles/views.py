from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView

from circles.serializers import CircleSerializer
from circles.models import Circle

User = get_user_model()


# List all users: api/circles/list/
class ListCirclesAPIView(ListAPIView):
    serializer_class = CircleSerializer
    queryset = Circle.objects.all()
    permission_classes = []

