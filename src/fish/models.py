from django.db import models
from django.conf import settings
import uuid


class Gender(models.Model):
    """Модель гендеру риби"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Species(models.Model):
    """Модель виду риби і равлика"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Fish(models.Model):
    """Модель риби"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.species} - {self.quantity}'


class Algae(models.Model):
    """Модель водоростей"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.species} - {self.quantity}'


class Shrimp(models.Model):
    """Модель креветок"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.species} - {self.quantity}'


class Aquarium(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    fish = models.ManyToManyField(Fish, blank=True)
    algae = models.ManyToManyField(Algae, blank=True)
    shrimp = models.ManyToManyField(Shrimp, blank=True)
    last_eat = models.DateTimeField(auto_now_add=True)
    last_clean = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.last_eat}'
