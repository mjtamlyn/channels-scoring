import json

from channels import Group

from .models import Game, RoundScore


def _round_scores_for_game(game):
    data = []
    rounds = range(1, game.number_of_rounds + 1)
    for score in game.score_set.all():
        round_scores = {s.round_number: s.value for s in score.roundscore_set.all()}
        for r in rounds:
            data.append({
                'score': score.pk,
                'round': r,
                'value': round_scores.get(r, None),
            })
    return data


def data_entry_connect(message, game_id):
    game = Game.objects.get(pk=game_id)  # Or 404?
    Group('data-entry-%s' % game_id).add(message.reply_channel)
    message.reply_channel.send({
        'text': json.dumps({
            'status': 'Connected to %s data entry' % game,
            'data': _round_scores_for_game(game)
        })
    })


def data_entry_receive(message, game_id):
    game = Game.objects.get(pk=game_id)
    group = Group('data-entry-%s' % game_id)
    data = json.loads(message['text'])
    round_score, created = RoundScore.objects.get_or_create(
        score__game=game,
        score_id=data['score'],
        round_number=data['round'],
        defaults={'value': data['value']},
    )
    if not created:
        round_score.value = data['value']
        round_score.save()
    group.send({
        'text': json.dumps({
            'data': _round_scores_for_game(game)
        })
    })


def data_entry_disconnect(message, game_id):
    Group('data-entry-%s' % game_id).discard(message.reply_channel)
