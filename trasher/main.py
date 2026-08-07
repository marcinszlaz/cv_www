from flask import Flask, request, url_for, render_template
from markupsafe import escape, Markup


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "<p><h1>Hello, World!</h1></p>"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"<h1>Hello, {escape(name)}!</h1>"
    #return f"<h1>Hello, {(name)}!</h1>"

@app.route("/user/<string:username>")
def profile(username):
    return f"<h2>{username}\'s profile</h2>"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return "login by POST"
    else:
        return "login by GET"
# Alternative for methods=[...]
# @app.get() and @app.post() decorators

with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello"))
    print(url_for("profile", username="Marcin s s"))
    print(url_for("login", next="/"))

@app.route("/hello-1/")
@app.route("/hello-1/<string:name>")
def hello_1(name=None):
    return render_template("hello.html", person=name)


