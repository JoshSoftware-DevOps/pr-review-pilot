from flask import Flask, jsonify

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

@app.route("/users/search")
def search_users():
    query = request.args.get("name")
    result = [u for u in users.values() if query in u["name"]]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
