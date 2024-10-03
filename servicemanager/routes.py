from flask import render_template, request, redirect, url_for
from servicemanager import app, db
from servicemanager.models import Customer, Service

@app.route("/")
def home():
    return render_template("services.html")


@app.route("/customers")
def customers():
    customers = list(Customer.query.order_by(Customer.customer_name).all())
    return render_template("customers.html", customers=customers)


@app.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        customer = Customer(customer_name=request.form.get("customer_name"))
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("customers"))
    return render_template("add_customer.html")


@app.route("/update_customer/<int:customer_id>", methods=["GET", "POST"])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if request.method == "POST":
        customer.customer_name = request.form.get("customer_name")
        db.session.commit()
        return redirect(url_for("customers"))
    return render_template("update_customer.html", customer=customer)


@app.route("/delete_customer/<int:customer_id>")
def remove_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("customers"))

