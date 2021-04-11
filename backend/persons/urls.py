from django.urls import path

from persons.views import ListUsersAPIView

urlpatterns = [
    path('me/', ListUsersAPIView.as_view()),
]
