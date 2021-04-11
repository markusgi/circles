from django.urls import path

from persons.views import ListPersonsAPIView, RetrieveUpdateDestroyPersonAPIView

urlpatterns = [
    path('list/', ListPersonsAPIView.as_view()),
    path('<int:id>/', RetrieveUpdateDestroyPersonAPIView.as_view()),
]
