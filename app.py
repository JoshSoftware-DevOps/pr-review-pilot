# trigger review test 
# retest 21 sept
from flask import Flask, jsonify, request, render_template_string

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

@app.route("/users/<int:user_id>/update", methods=["POST"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "not found"}), 404
    data = request.get_json()
    requesting_user = request.args.get("as_user", type=int)
    if requesting_user is None:
        return jsonify({"error": "as_user required"}), 400
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify(users[user_id])


@app.route("/greet")
def greet():
    name = request.args.get("name", "friend")
    return render_template_string(f"<h1>Hello {name}!</h1>")

if __name__ == "__main__":
    app.run(debug=True)
