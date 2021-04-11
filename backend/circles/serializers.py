from django.contrib.auth import get_user_model
from rest_framework import serializers
from circles.models import Circle

User = get_user_model()


class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = '__all__'

