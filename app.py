from flask import Flask, request, jsonify

app = Flask(__name__)

PASSWORD = "your_password"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data.get("password") == PASSWORD:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run()
