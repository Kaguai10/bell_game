from flask import Flask, render_template, request, jsonify
from datetime import datetime
import threading

app = Flask(__name__)
buzzed_players = []
reset_version = 0
lock = threading.Lock()

@app.route('/')
def index():
    return render_template('server.html', buzzed=buzzed_players)

@app.route('/player/<int:player_id>')
def player(player_id):
    return render_template('player.html', player_id=player_id)

@app.route('/buzz', methods=['POST'])
def buzz():
    global buzzed_players
    player_id = request.json.get('player_id')
    with lock:
        if player_id not in [p['id'] for p in buzzed_players]:
            buzzed_players.append({
                'id': player_id,
                'timestamp': datetime.now().isoformat()
            })
            return jsonify(position=len(buzzed_players))
    return jsonify(position=None)

@app.route('/buzzed')
def get_buzzed():
    return jsonify(buzzed_players)

@app.route('/reset', methods=['POST'])
def reset():
    global buzzed_players, reset_version
    with lock:
        buzzed_players = []
        reset_version += 1
    return '', 204

@app.route('/reset_status')
def reset_status():
    return jsonify(reset_version=reset_version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
