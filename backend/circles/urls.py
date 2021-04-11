from django.urls import path

from circles.views import ListCirclesAPIView, RetrieveUpdateDestroyCircleAPIView

urlpatterns = [
    path('list/', ListCirclesAPIView.as_view()),
    path('<int:id>/', RetrieveUpdateDestroyCircleAPIView.as_view()),
]
