from flask import Flask, jsonify, request
from pythontraining.flask.server.database import Database

app = Flask(__name__)
app.config.from_object(__name__)
database = Database()

@app.route("/")
def index():
    data = {
        "cats": 5,
        "people": 8,
        "dogs": 4
    }
    return jsonify(data)

@app.route("/send_me_data", methods=["POST"])
def send_me_data():
    data = request.form
    for key, value in data.items():
        print("received", key, "with value", value)
    return "Thanks"

@app.route("/get_all_users")
def get_all_users():
    all_users = database.get_all_users()
    return jsonify(all_users)

@app.route("/add_user")
def add_user():
    data = request.form
    username = data["username"]
    real_name = data["real_name"]
    database.add_user(username, real_name)
    return jsonify(
        "User Created"
    )

@app.route("/user_exists", methods=["POST"])
def user_exists():
    username = request.form.get("username")
    exists = database.user_exists(username)

    return jsonify({
        "exists": exists
    })


if __name__ == '__main__':
    app.run(debug=True)




