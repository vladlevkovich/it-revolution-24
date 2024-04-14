FROM python:3.11

RUN mkdir /downloader

WORKDIR /downloader

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV ROOT_URLCONF=aquarium.urls

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
