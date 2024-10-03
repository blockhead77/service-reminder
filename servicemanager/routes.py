from flask import render_template
from servicemanager import app, db
from servicemanager.models import Customer, Service

@app.route("/")
def home():
    return render_template("base.html")
