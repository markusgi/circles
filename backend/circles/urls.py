from django.urls import path

from circles.views import ListCirclesAPIView

urlpatterns = [
    path('list/', ListCirclesAPIView.as_view()),
]
