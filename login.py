from flask import Flask, render_template
from flask_socketio import SocketIO
from user import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app)

@app.route("/api/login", methods=["POST"])
def login() -> int:
    