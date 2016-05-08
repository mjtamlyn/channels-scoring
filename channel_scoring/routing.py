from channels.routing import include

import scoring.routing


routes = [
    include(scoring.routing.routes, path='^/websocket/'),
]
