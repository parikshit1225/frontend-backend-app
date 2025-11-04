from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests (enable carefully in production)

@app.route("/api/hello", methods=["POST"])
def hello():
    data = request.get_json()
    name = data.get("name", "User")
    return jsonify({"message": f"Hello, {name}! This response is from the backend (private subnet)."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)