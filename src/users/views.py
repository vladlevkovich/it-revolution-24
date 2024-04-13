from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserAuthSerializer
from .authentication import JWTAuthentication
from .models import CustomUser


class UserRegister(generics.GenericAPIView):
    """Реєстрація користувача"""
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user = CustomUser.objects.filter(email=email)
        if user:
            return Response({'message': 'Such a user exists'}, status=status.HTTP_409_CONFLICT)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthUser(generics.GenericAPIView):
    """Логін користувача і створення токенів"""
    serializer_class = UserAuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        password = serializer.data['password']
        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'message': 'Invalid input data'}, status=status.HTTP_400_BAD_REQUEST)

        access_token = JWTAuthentication.create_access(user)
        refresh_token = JWTAuthentication.create_refresh(user)
        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token
        })
