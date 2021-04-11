from django.contrib.auth import get_user_model
from rest_framework import serializers

from persons.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

