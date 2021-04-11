from django.db import models
from persons.models import Person

class Circle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    lead = models.ForeignKey(to=Person, on_delete=models.CASCADE, blank=True, related_name="circle_lead")
    members = models.ManyToManyField(to=Person, blank=True, related_name="circle_member")

    def __str__(self):
        return self.name