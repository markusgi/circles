from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Circle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    lead = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, related_name="circle_lead")
    members = models.ManyToManyField(to=User, blank=True, related_name="circle_member")

    def __str__(self):
        return self.name