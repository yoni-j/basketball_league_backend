from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from league.choices import StageChoices, ResultChoices

# Create your models here.
from teams.models import Team, Player


class League(models.Model):
    name = models.CharField(max_length=200, default="Champions League")


class Round(models.Model):
    league = models.ForeignKey(League, related_name="rounds", on_delete=models.CASCADE)
    stage = models.IntegerField(choices=StageChoices.choices)


class Game(models.Model):
    round = models.ForeignKey(Round, related_name="games", on_delete=models.CASCADE)


class GameTeam(models.Model):
    game = models.ForeignKey(Game, related_name="teams", on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name="games", on_delete=models.CASCADE)
    result = models.CharField(choices=ResultChoices.choices, max_length=5, null=True)


class GamePlayer(models.Model):
    game = models.ForeignKey(Game, related_name="players", on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name="games_played", on_delete=models.CASCADE, null=True)
    score = models.IntegerField()
