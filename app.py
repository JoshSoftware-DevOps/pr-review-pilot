from flask import Flask, jsonify, request
from validators import is_valid_email

app = Flask(__name__)

users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify({"error": "not found"}), 404
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    if not is_valid_email(email):
        return jsonify({"error": "invalid email"}), 400
    user["email"] = email
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "not found"}), 404
    del users[user_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
