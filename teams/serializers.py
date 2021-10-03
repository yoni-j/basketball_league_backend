from django.db.models import Avg
from rest_framework import serializers

from league.models import GamePlayer
from teams.models import Player


class PlayersListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['user','team', 'pk']

    def get_user(self, obj):
        return obj.user.username

    def get_team(self, obj):
        return obj.team.name


class PlayerDetailsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    avg_score = serializers.SerializerMethodField()
    played_games = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['name', 'height', 'played_games', 'avg_score']

    def get_avg_score(self, obj):
        return GamePlayer.objects.filter(player=obj).aggregate(Avg('score'))['score__avg']

    def get_name(self, obj):
        return obj.user.username

    def get_played_games(self, obj):
        return obj.games_played.count()
