from flask import Blueprint, render_template
from flask_login import login_required

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/", endpoint="index")
@login_required
def index_page():
    return render_template("index.html")
