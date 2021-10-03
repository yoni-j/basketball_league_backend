from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.views import TokenViewBase
from teams.models import Coach


class CustomTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        try:
            coach = Coach.objects.get(pk=self.user.pk)
            data['is_coach'] = True
        except ObjectDoesNotExist:
            data['is_coach'] = False

        return data


class CustomTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = CustomTokenObtainPairSerializer
