from django.db import models
from src.users.models import CustomUser
from django.urls import reverse
from django.conf import settings
import uuid


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])
