from django.conf.urls import url

from . import views


urlpatterns = [
    url('^$', views.GameList.as_view(), name='index'),
    url('^(?P<game_id>\d+)/$', views.GameLeaderboard.as_view(), name='leaderboard'),
    url('^(?P<game_id>\d+)/score/$', views.GameDataEntry.as_view(), name='data-entry'),
]
