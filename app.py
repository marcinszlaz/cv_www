from flask import Flask, request, url_for, render_template
from markupsafe import escape, Markup

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", borders=10)

@app.route("/grid")
def grid():
    return render_template("grid.html")

if __name__ == "main":
    app.run(debug=True, host="0.0.0.0", port=80)


