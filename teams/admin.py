from django.contrib import admin
from teams.models import Team, Player, Coach

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)