
from rest_framework import serializers
from circles.models import Circle

class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = '__all__'

