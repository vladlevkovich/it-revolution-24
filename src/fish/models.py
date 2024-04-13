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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    algae = models.ForeignKey(Algae, on_delete=models.CASCADE)
    shrimp = models.ForeignKey(Shrimp, on_delete=models.CASCADE)
    last_eaten = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


# class Aquarium(models.Model):
#     """Модель акваріуму"""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.PROTECT)
#     type_fish = models.ForeignKey(Species, blank=True, null=True, on_delete=models.PROTECT)
#     count = models.IntegerField(default=1)

    # def __str__(self):
    #     return f'{self.type_fish} - {self.count}'
