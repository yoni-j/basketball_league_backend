from django.contrib import admin
from league.models import League, Round, Game, GameTeam, GamePlayer

# Register your models here.
admin.site.register(League)
admin.site.register(Round)
admin.site.register(Game)
admin.site.register(GameTeam)
admin.site.register(GamePlayer)