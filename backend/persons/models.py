from django.db import models
from django.conf import settings

class Person(models.Model):
    email = models.EmailField(
        verbose_name="email",
        unique=True,
        max_length=60,
        blank=True,
    )
    vorname = models.CharField(
        verbose_name='vorname',
        max_length=60,
        blank=True,
    )
    nachname = models.CharField(
        verbose_name='nachname',
        max_length=60,
        blank=True,
    )
    anstellungsart = models.CharField(
        verbose_name='anstellungsart',
        max_length=60,
        blank=True,
    )    
    standort = models.CharField(
        verbose_name='standort',
        max_length=60,
        blank=True,
    )    
    team = models.CharField(
        verbose_name='team',
        max_length=60,
        blank=True,
    )
    position = models.CharField(
        verbose_name='position',
        max_length=60,
        blank=True,
    )
    # das wäre wahrscheinlich foreign Key
    # dann beim import mit Person.objects.get_or_create(...)
    vorgesetzter = models.CharField(
        verbose_name='vorgesetzter',
        max_length=60,
        blank=True,
    )

    def __str__(self):
        return self.vorname

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
