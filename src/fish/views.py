from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .serializers import *
from .models import *


class FeedAquarium(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        try:
            aquarium = Aquarium.objects.get(user=request.user)
        except Aquarium.DeosNotExist:
            return Response({'message': 'Aquarium not found'}, status=status.HTTP_404_NOT_FOUND)

        aquarium.last_eat = timezone.now()
        aquarium.save()
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)


class AquariumReadCreate(generics.GenericAPIView):
    serializer_class = ResidentSerializer

    def get(self, request):
        aquarium = Aquarium.objects.get(user=request.user)
        serializer = self.serializer_class(aquarium)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print('USER', request.user)
        serializer = self.serializer_class(data=request.data, context={'request': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
