from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .serializers import *
from .models import *


class FeedAquarium(generics.GenericAPIView):
    """годуємо рибок в акваріумі"""
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        try:
            aquarium = Aquarium.objects.filter(user=request.user).first()
        except Aquarium.DeosNotExist:
            return Response({'message': 'Aquarium not found'}, status=status.HTTP_404_NOT_FOUND)

        aquarium.last_eat = timezone.now()
        aquarium.save()
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)


class AddFish(generics.GenericAPIView):
    serializer_class = AddFishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print(request.user)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddAlgae(generics.GenericAPIView):
    serializer_class = AddAlgaeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddShrimp(generics.GenericAPIView):
    serializer_class = AddShrimpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AquariumReadCreate(generics.GenericAPIView):
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        aquarium = Aquarium.objects.filter(user=request.user).first()
        serializer = self.serializer_class(aquarium)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print('USER', request.user)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
