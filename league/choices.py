from django.db import models


class StageChoices(models.IntegerChoices):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4


class ResultChoices(models.TextChoices):
    WON = "Won"
    LOST = "Lost"
