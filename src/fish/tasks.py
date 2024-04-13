from aquarium.worker import app
from django.utils import timezone
from datetime import timedelta
from src.fish.models import Aquarium


@app.task()
def notification_eaten():
    aquariums = Aquarium.objects.all()
    for aquarium in aquariums:
        if timezone.now() - aquarium.last_eat > timedelta(days=1):
            pass
