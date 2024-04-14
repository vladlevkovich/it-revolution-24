from django.http import HttpResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .models import *
import json
import requests


class Analytics(generics.GenericAPIView):
    serializer_class = AllFishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        male_fish = Fish.objects.filter(is_male=True, user=request.user).count()
        girl_fish = Fish.objects.filter(is_male=False, user=request.user).count()
        live_fish = Fish.objects.filter(is_death=False, user=request.user).count()
        fish_death = Fish.objects.filter(is_death=True, user=request.user).count()

        algae = Snail.objects.filter(is_death=False, user=request.user).count()
        algae_male = Snail.objects.filter(is_male=True, user=request.user).count()
        algae_girl = Snail.objects.filter(is_male=False, user=request.user).count()
        algae_death = Snail.objects.filter(is_death=True, user=request.user).count()

        live_shrimp = Shrimp.objects.filter(is_death=False, user=request.user).count()
        shrimp_death = Shrimp.objects.filter(is_death=True, user=request.user).count()
        shrimp_male = Shrimp.objects.filter(is_male=True, user=request.user).count()
        shrimp_girl = Shrimp.objects.filter(is_male=False, user=request.user).count()

        fish_data = {
            'live': live_fish,
            'dead': fish_death,
            'male': male_fish,
            'girl': girl_fish
        }
        algae_data = {
            'live': algae,
            'dead': algae_death,
            'male': algae_male,
            'girl': algae_girl
        }
        shrimp_data = {
            'live': live_shrimp,
            'dead': shrimp_death,
            'male': shrimp_male,
            'girl': shrimp_girl
        }
        return Response(
            {
                'fish': fish_data,
                'algae': algae_data,
                'shrimp': shrimp_data,
            },
            status=status.HTTP_200_OK
        )


class FeedAquarium(generics.CreateAPIView):
    """Годуємо рибок в акваріумі"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EatRecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response({'message': 'Eat record created successfully'}, status=status.HTTP_201_CREATED)


class CleanAquarium(generics.CreateAPIView):
    """Чистка акваріуму"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CleanAquariumRecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response({'message': 'Clean aquarium record created successfully'}, status=status.HTTP_201_CREATED)


class AddFish(generics.GenericAPIView):
    serializer_class = AddFishSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'gender': openapi.Schema(type=openapi.TYPE_STRING),
                'species': openapi.Schema(type=openapi.TYPE_STRING),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
        ),
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_='header',
                type='string',
                required=True,
                description='Bearer token required for authentication',
                example='Bearer YOUR_TOKEN',
            )
        ]
    )
    def post(self, request):
        # print(request.user)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FishUpdate(generics.UpdateAPIView):
    serializer_class = UpdateFishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        fish_id = self.kwargs.get('pk')
        return Fish.objects.get(user=self.request.user, id=fish_id)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddSnail(generics.GenericAPIView):
    serializer_class = AddSnailSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'species': openapi.Schema(type=openapi.TYPE_STRING),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
        ),
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_='header',
                type='string',
                required=True,
                description='Bearer token required for authentication',
                example='Bearer YOUR_TOKEN',
            )
        ]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AlgaeUpdate(generics.UpdateAPIView):
    serializer_class = UpdateSnailSerializer

    def get_queryset(self):
        algae_id = self.kwargs.get('pk')
        return Snail.objects.get(id=algae_id, user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddShrimp(generics.GenericAPIView):
    serializer_class = AddShrimpSerializer

    @swagger_auto_schema(
        # method='POST',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'species': openapi.Schema(type=openapi.TYPE_STRING),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
        ),
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_='header',
                type='string',
                required=True,
                description='Bearer token required for authentication',
                example='Bearer YOUR_TOKEN',
            )
        ]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShrimpUpdate(generics.UpdateAPIView):
    serializer_class = UpdateShrimpSerializer

    def get_queryset(self):
        shrimp_id = self.kwargs.get('pk')
        return Shrimp.objects.get(id=shrimp_id, user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AquariumReadCreate(generics.GenericAPIView):
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_='header',
                type='string',
                required=True,
                description='Bearer token required for authentication',
                example='Bearer YOUR_TOKEN',
            )
        ]
    )
    def get(self, request):
        aquarium = Aquarium.objects.filter(user=request.user).first()
        serializer = self.serializer_class(aquarium)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_='header',
                type='string',
                required=True,
                description='Bearer token required for authentication',
                example='Bearer YOUR_TOKEN',
            )
        ]
    )
    def post(self, request):
        print('USER', request.user)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def downland_swagger(request):
    url = 'http://127.0.0.1:8000/swagger.json'
    response = requests.get(url)

    if response.status_code == 200:
        json_schema = response.json()
        json_string = json.dumps(json_schema, indent=4)

        filename = 'banyak.json'
        response = HttpResponse(json_string, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
    else:
        return HttpResponse(status=response.status_code)

