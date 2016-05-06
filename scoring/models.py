from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50)
    number_of_rounds = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Score(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    score = models.PositiveIntegerField(default=0, editable=False)
    position = models.PositiveIntegerField(default=1, editable=False)

    class Meta:
        unique_together = ('game', 'player')

    def __str__(self):
        return '%s playing %s' % (self.player, self.game)


class RoundScore(models.Model):
    score = models.ForeignKey(Score)
    round_number = models.PositiveIntegerField()
    value = models.PositiveIntegerField()

    class Meta:
        unique_together = ('score', 'round_number')

    def __str__(self):
        return 'Round %s in score %s' % (self.round_number, self.score_id)
