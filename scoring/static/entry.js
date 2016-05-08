document.addEventListener('DOMContentLoaded', function(event) { 
    var ws_scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
    var socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + '/websocket' + window.location.pathname);

    socket.onmessage = function(message) {
        var data = JSON.parse(message.data);

        data.data.forEach(function(score) {
            var input = document.querySelectorAll('[data-score="' + score.score + '"][data-round="' + score.round + '"]')[0];
            input.value = score.value;
        });
    };

    Array.prototype.slice.call(document.querySelectorAll('[data-score]')).forEach(function(element) {
        element.addEventListener('blur', function(event) {
            if (this.value) {
                socket.send(JSON.stringify({
                    'score': this.dataset.score,
                    'round': this.dataset.round,
                    'value': this.value,
                }));
            }
        });
    });
});
