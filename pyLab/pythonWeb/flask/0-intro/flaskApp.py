from flask import Flask, redirect, url_for

#Create flack web app
app = Flask(__name__)


#define how we can access the home page
@app.route("/")
# define home page
def home():
    return "Hello, that is home page. <h1> HELLO </h1>"

@app.route("/<name>")
def user(name):
    return f" HEllo {name} !"

#redirrecting 
@app.route("/admin/")
def admin():
    return redirect(url_for("home"))

#redirrecting specific funtion taking argument
#@app.route("/admin")
#def admin():
#    return redirect(url_for("user", name ="Admin!"))

if __name__ == "__main__":
    app.run()