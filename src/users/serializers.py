from rest_framework import serializers
from .models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        print(password)
        user = CustomUser.objects.create(email=email)
        user.set_password(password)
        user.save()
        return user


class UserAuthSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class UpdateAccessTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(min_length=1)
