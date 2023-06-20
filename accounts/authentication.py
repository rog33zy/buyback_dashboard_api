import jwt

from django.conf import settings

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from .models import User


class SafeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get("Authorization")

        if not authorization_header:
            return None

        try:
            access_token = authorization_header.split(" ")[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("access_token expired")

        except IndexError:
            raise exceptions.AuthenticationFailed("Token prefix missing")

        user = payload["user"]

        is_authenticated = user["is_authenticated"]
        is_active = user["is_active"]
        is_foundation_farm_admin = user["is_foundation_farm_admin"]
        is_commercial_farmers_admin = user["is_commercial_farmers_admin"]
        is_field_finance_admin = user["is_field_finance_admin"]
        is_malawi_admin = user["is_malawi_admin"]

        user = User(
            is_authenticated=is_authenticated,
            is_active=is_active,
            is_foundation_farm_admin=is_foundation_farm_admin,
            is_commercial_farmers_admin=is_commercial_farmers_admin,
            is_field_finance_admin=is_field_finance_admin,
            is_malawi_admin=is_malawi_admin,
        )

        return (user, None)
