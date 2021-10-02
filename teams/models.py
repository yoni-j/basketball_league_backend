from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def is_coach(self):
        try:
            coach = Coach.objects.get(pk=self.pk)
            return True
        except ObjectDoesNotExist:
            return False

    def is_player(self):
        try:
            player = Player.objects.get(pk=self.pk)
            return True
        except ObjectDoesNotExist:
            return False

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=200)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, related_name="players", on_delete=models.CASCADE)
    height = models.IntegerField()
    

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
