from flask import Flask, redirect, url_for, render_template

# first we have to create a forder and name it as "templates"
app = Flask(__name__)

#@app.route("/")
#def home():
#    return render_template("index.html")

#@app.route("/<name>")
#def home(name):
#    return render_template("index.html", content=name)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["e", "ee", "eee", "eeee", "eeeee"])



if __name__ == "__main__":
    app.run()