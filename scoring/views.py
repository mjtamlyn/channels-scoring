from django.views.generic import DetailView, ListView

from .models import Game


class GameList(ListView):
    model = Game
    template_name = 'index.html'


class GameLeaderboard(DetailView):
    model = Game
    pk_url_kwarg = 'game_id'
    template_name = 'leaderboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scores'] = self.object.score_set.order_by('-position').select_related('player')
        return context


class GameDataEntry(DetailView):
    model = Game
    pk_url_kwarg = 'game_id'
    template_name = 'data_entry.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scores'] = self.object.score_set.order_by('-position').select_related('player').prefetch_related('roundscore_set')
        context['rounds'] = range(1, self.object.number_of_rounds + 1)
        for score in context['scores']:
            round_scores = {s.round_number: s.value for s in score.roundscore_set.all()}
            score.round_scores = []
            for r in context['rounds']:
                score.round_scores.append(round_scores.get(r, None))
        return context
