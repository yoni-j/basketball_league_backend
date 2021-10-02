from django.db.models import Avg
from rest_framework import serializers

from league.models import GamePlayer
from teams.models import Player


class PlayersListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['user', 'height']

    def get_user(self, obj):
        return obj.user.username


class PlayerDetailsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    avg_score = serializers.SerializerMethodField()
    played_games = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['user', 'height', 'played_games', 'avg_score']

    def get_avg_score(self, obj):
        return GamePlayer.objects.filter(player=obj).aggregate(Avg('score'))['score__avg']

    def get_user(self, obj):
        return obj.user.username

    def get_played_games(self, obj):
        return obj.games_played.count()
