from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView

from persons.serializers import PersonSerializer
from persons.models import Person


# List all users: api/users/list/
class ListPersonAPIView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = []
