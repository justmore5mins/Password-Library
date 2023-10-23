from flask import Flask, request
from user import *

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login() -> int:
    username = request.form["username"]
    password = request.form["password"]
    print(f"User {username} log in by password {password}")
    
if __name__ == "__main__":
    app.run(debug=True,port=5500)