from django.db.models import Avg, Sum
from rest_framework import serializers

from league.models import GamePlayer, Game, GameTeam, Round, League
from teams.models import Player


class TeamSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = GameTeam
        fields = ['team_name', 'result', 'score']

    def get_score(self, obj):
        return GamePlayer.objects.filter(game=obj.game, player__team=obj.team).aggregate(Sum('score'))['score__sum']

    def get_team_name(self, obj):
        return obj.team.name


class GameSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    class Meta:
        model = Game
        fields = ['teams']

class RoundSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True)
    class Meta:
        model = Round
        fields = ['stage', 'games']


class LeagueSerializer(serializers.ModelSerializer):
    rounds = RoundSerializer(many=True)
    class Meta:
        model = League
        fields = ['name', 'rounds']


# class PlayersListSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Player
#         fields = ['user', 'height']
#
#     def get_user(self, obj):
#         return obj.user.username
#
#
# class PlayerDetailsSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#     avg_score = serializers.SerializerMethodField()
#     played_games = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Player
#         fields = ['user', 'height', 'played_games', 'avg_score']
#
#     def get_avg_score(self, obj):
#         return GamePlayer.objects.filter(player=obj).aggregate(Avg('score'))['score__avg']
#
#     def get_user(self, obj):
#         return obj.user.username
#
#     def get_played_games(self, obj):
#         return obj.games_played.count()
