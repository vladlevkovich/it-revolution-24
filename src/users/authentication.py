from datetime import datetime, timedelta
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser
import jwt


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return None

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)

        try:
            payload = jwt.decode(jwt_token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except Exception as e:
            return str(e)

        email = payload.get('email')
        if email is None:
            raise AuthenticationFailed('User identifier not found in JWT')

        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        return user, payload

    @classmethod
    def create_access(cls, user):
        payload = {
            'user_id': str(user.id),
            'email': user.email,
            'user_first_name': user.first_name,
            'user_last_name': user.last_name,
            'exp': datetime.utcnow() + timedelta(days=1),
            'type': 'access'
        }
        access_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
        return access_token

    @classmethod
    def create_refresh(cls, user):
        payload = {
            'user_id': str(user.id),
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(days=2),
            'type': 'refresh'
        }
        refresh_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
        return refresh_token

    @classmethod
    def update_access_token(cls, refresh_token: str):
        try:
            payload = jwt.decode(refresh_token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
            if payload.get('type') != 'refresh':
                raise jwt.DecodeError('Invalid token type')
        except jwt.exceptions.DecodeError:
            raise AuthenticationFailed('Invalid token')
        except jwt.exceptions.InvalidTokenError:
            raise AuthenticationFailed('Invalid signature')
        except jwt.exceptions.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except Exception as e:
            return str(e)

        user_id = payload.get('user_id')
        user = CustomUser.objects.get(id=user_id)

        if not user:
            raise AuthenticationFailed('User not found')

        access_token = cls.create_access(user)
        return access_token

    @classmethod
    def get_the_token_from_header(cls, token: str):
        token = token.replace('Bearer', '').replace(' ', '')
        return token
