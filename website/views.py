from flask import Blueprint, render_template
from flask_login import login_required, current_user
# create a new blueprint, which defines how the website can be accessed
views = Blueprint('views',__name__,)




@views.route("/")
def base():
    temp = render_template("base.html")
    return temp

variable = "variables can be passed this way"

@views.route("/map/")
@login_required
def map():
    temp = render_template("map.html", foo = variable)
    return temp





