from flask import Flask, redirect, url_for, render_template, request, session, flash
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!   REMEMBER THAT                                              !!!
#!!!   USE : 'pip install flask-sqlalchemy'                       !!!
#!!!   BEFORE WORKING WITH SqlAlchemy DATABASE                    !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#importing SQLAlchemy Database Library
from flask_sqlalchemy import SQLAlchemy
#
app = Flask(__name__)
#
# Setting up database object
db = SQLAlchemy(app)
# configure sqllite database
# users.sqlite3 : user is name of the database table
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
# do not tracking modifications on database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# we are going to define a class whis is gonna represent user object in our database
class users(db.Model):
# Every single objects we have in database needs to have unique identification
# identification could be string, boolean, integer whatever we wants but it must be uniqe   
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email
#
app.secret_key = "enivicivokki"
#
from datetime import timedelta
# we are gonna store our permanent session data for 5 minutes
app.permanent_session_lifetime = timedelta(minutes = 5)
# if we do not set that our session data is going to be deleted after closing the web browser
#
@app.route("/")
def home():
    return render_template("index.html")
#
#
@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())
#
#
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # that defines these sessions are permanent sessions
        user = request.form["nm"]
        session["user"] = user


#
#
# To delete one specific object in dataase : 
# found_user = users.query.filter_by(name = user).delete()
# If we wanna delete multiple lines we have to loop throuhgh  : : 
#       found_user = users.query.filter_by(name = user).delete()
#       for user in found_user:
#           user.delete()
#
#
        found_user = users.query.filter_by(name = user).first() 
        if found_user  :
            session["email"] = found_user.email
        else :
            usr = users(user,None)
            db.session.add(usr)
            db.session.commit()

        flash("Login Succesfull!")
        return redirect(url_for("user"))
    else :
        if "user" in session : 
            flash("Already Logged In!")
            return redirect(url_for("user"))
        else:
            flash("You Are Not Logged In!")
            
        return render_template("login.html")
#
#
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    user = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            # If we wanna change user email
            found_user = users.query.filter_by(name = user).first() 
            found_user.email = email
            db.session.commit()
            flash("Email Was Saved!")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html",user=user, email=email)
    else:
        return redirect(url_for("login"))
#
#
@app.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))
#
#
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)