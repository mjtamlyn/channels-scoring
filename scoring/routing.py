from channels.routing import route

from . import consumers


routes = [
    route('websocket.connect', consumers.data_entry_connect, path='^(?P<game_id>\d+)/score/$'),
    route('websocket.receive', consumers.data_entry_receive, path='^(?P<game_id>\d+)/score/$'),
    route('websocket.disconnect', consumers.data_entry_disconnect, path='^(?P<game_id>\d+)/score/$'),
]
