from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)