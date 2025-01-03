from flask import Blueprint, render_template
# blueprint means it has a bunch of urls inside

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("home.html")


