from django.urls import path

from persons.views import ListPersonAPIView

urlpatterns = [
    path('me/', ListPersonAPIView.as_view()),
]
