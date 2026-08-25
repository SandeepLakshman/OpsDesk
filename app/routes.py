from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Incident

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():
    incidents = Incident.query.order_by(Incident.id.desc()).all()
    return render_template("dashboard.html", incidents=incidents)


@main.route("/incidents", methods=["GET", "POST"])
def incidents():
    if request.method == "POST":
        incident = Incident(
            title=request.form["title"],
            description=request.form["description"],
            priority=request.form["priority"]
        )
        db.session.add(incident)
        db.session.commit()
        return redirect(url_for("main.incidents"))

    incidents = Incident.query.order_by(Incident.id.desc()).all()
    return render_template("incidents.html", incidents=incidents)