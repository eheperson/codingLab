from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="templates",)

@second.route("/home/")
@second.route("/")
def home():
    return "<h1> That is the admin page </h1>"


@second.route("/test/")
def test():
    return "<h1> Test page </h1>"