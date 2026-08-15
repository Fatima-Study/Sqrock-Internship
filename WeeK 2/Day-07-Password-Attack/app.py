from flask import Flask, request

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "password123"


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return "Welcome! Login successful."

    return "Invalid username or password.", 401


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)