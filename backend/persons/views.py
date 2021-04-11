from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from persons.serializers import PersonSerializer
from persons.models import Person


# List all users: api/persons/list/
class ListPersonsAPIView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = []

# List all users: api/persons/int:id/
class RetrieveUpdateDestroyPersonAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = []
    lookup_field = 'id'
