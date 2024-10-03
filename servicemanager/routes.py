from flask import render_template, request, redirect, url_for
from servicemanager import app, db
from servicemanager.models import Customer, Service

@app.route("/")
def home():
    return render_template("services.html")


@app.route("/customers")
def customers():
    return render_template("customers.html")


@app.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        customer = Customer(customer_name=request.form.get("customer_name"))
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("customers"))
    return render_template("add_customer.html")
