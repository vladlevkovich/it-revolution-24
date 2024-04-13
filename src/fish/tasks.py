from aquarium.worker import app


@app.task()
def notification_eaten():
    pass
