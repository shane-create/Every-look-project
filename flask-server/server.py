from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO!"

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "main":
    app.run(debug = True)