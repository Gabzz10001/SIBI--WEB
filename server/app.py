from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sibi-key-2024'
socketio = SocketIO(app, cors_allowed_origins="*")

# ================= STORAGE DATA =================
latest_data = {
    "huruf": "",
    "kata": "",
    "teks": ""
}

# ================= WEB =================
@app.route("/")
def index():
    return render_template("index.html")

# ================= RECEIVE DATA FROM AI (LAPTOP) =================
@app.route("/update", methods=["POST"])
def update():
    global latest_data

    try:
        data = request.json

        latest_data = {
            "huruf": data.get("huruf", ""),
            "kata": data.get("kata", ""),
            "teks": data.get("teks", "")
        }

        return jsonify({"success": True})

    except:
        return jsonify({"success": False})

# ================= SEND DATA TO FRONTEND =================
@app.route("/get_data")
def get_data():
    return jsonify(latest_data)

# ================= SOCKET EVENTS =================
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('response', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# ================= RUN =================
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host="0.0.0.0", port=port, debug=False)