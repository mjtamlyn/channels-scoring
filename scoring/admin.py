from django.contrib import admin

from .models import Game, Score, RoundScore, Player


admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Score)
admin.site.register(RoundScore)
