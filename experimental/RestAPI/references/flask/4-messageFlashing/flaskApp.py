from flask import Flask, redirect, url_for, render_template, request, session, flash
#
app = Flask(__name__)
#
# secret key is required for session
# we could write any string to string key
app.secret_key = "enivicivokki"
#
from datetime import timedelta
# we are gonna store our permanent session data for 5 days
app.permanent_session_lifetime = timedelta(days = 5)
app.permanent_session_lifetime = timedelta(minutes = 5)
# if we do not set that our session data is going to be deleted after closing the web browser
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!   REMEMBER THAT                                              !!!
#!!!   SESSIONS ARE TEMPORARY                                     !!!
#!!!   WE SHOULD NOT STORE SESSION DATA PERMANENTLY               !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
@app.route("/")
def home():
    return render_template("index.html")
#
#
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # that defines these sessions are permanent sessions
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else :
        if "user" in session : 
            return redirect(url_for("user"))
            
        return render_template("login.html")
#
#
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user} </h1>"
    else:
        return redirect(url_for("login"))
#
#
@app.route("/logout")
def logout():
    session.pop("user", None)
    # To flash a message
    # "info" is the message category
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))
#
#
if __name__ == "__main__":
    app.run(debug=True)