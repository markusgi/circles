from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView

from persons.serializers import UserSerializer

User = get_user_model()


# List all users: api/users/list/
class ListUsersAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
