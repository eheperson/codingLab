from flask import Flask, redirect, url_for, render_template, request, session
#
#Create flask web app
app = Flask(__name__)
#
## ---------------------------------------------------------------- ##
#  -----  Test Section - Begin  -------
#
# Define how we can access to page
@app.route("/test-for-flask")
#define a function what we see after accessing(requesting) to page
def testFcn():
    """
        That function is only for testing purpose
        to check if flask works correctly
    """
    return "Hello, that is test page. <h1> HELLO </h1>"
#
# Comment those lines after testing
# flask is confusing between "/<name>" and "/<usr>"
# @app.route("/<name>")
# def testArgument(name):
#     """
#         That function is only for testing purpose
#         to check if flask works correctly with variables
#     """
#     return f" HEllo {name} !"
#
#redirrecting to specific funtion taking argument
@app.route("/admin/")
def testRedirect():
    return redirect(url_for("testArgument"))
#    return redirect(url_for("user", name ="Admin!"))
#
# rendering a html page 
# to use html templates 
# first we have to create a folder and name it as "templates"
# flask searches html templates in "templates" folder
@app.route("/test-for-render")
def testRender():
    return render_template("index-test.html")
#
@app.route("/test-for-template-inheritance-index")
def testTemplateInheritance1():
    return render_template("index1.html")
    #return render_template("index.html", content=["e", "ee", "eee", "eeee", "eeeee"])
#
@app.route("/test-for-template-inheritance-new")
# that section of code is an example of template inheritance
def testTemplateInheritance2():
    return render_template("new.html", content = "Testing")
#
## HTML Methods 
@app.route("/test-html-methods", methods=["POST", "GET"])
def testMethods():
    # return render_template("login.html")
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("testUser", usr=user))
    else :
        return render_template("login.html")
#
@app.route("/<usr>")
def testUser(usr):
    #return "<h1> {usr} </h1>"
    return f"<h1> {usr} </h1>"
#
#
## Sessions 
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
@app.route("/test-session-login", methods=["POST", "GET"])
def testSessionLogin():
    if request.method == "POST":
        session.permanent = True # that defines these sessions are permanent sessions
        user = request.form["nm"]
        session["testSessionUser"] = user
        return redirect(url_for("testSessionUser"))
    else :
        if "testSessionUser" in session : 
            return redirect(url_for("testSessionUser"))
        return render_template("login.html")
#
@app.route("/test-session-user")
def testSessionUser():
    if "testSessionUser" in session:
        user = session["testSessionUser"]
        return f"<h1>{user} </h1>"
    else:
        return redirect(url_for("testSessionLogin"))
#
@app.route("/test-session-logout")
def testSessionLogout():
    session.pop("testSessionUser", None)
    return redirect(url_for("testSessionLogin"))
#  -----  Test Section - End  -------
## ---------------------------------------------------------------- ##
#



if __name__ == "__main__":
    app.run(debug=True)
