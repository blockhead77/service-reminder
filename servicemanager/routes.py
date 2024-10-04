from flask import render_template, request, redirect, url_for
from servicemanager import app, db
from servicemanager.models import Customer, Service

@app.route("/")
def home():
    services = list(Service.query.order_by(Service.id).all())
    return render_template("services.html", services=services)


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


@app.route("/add_service", methods=["GET", "POST"])
def add_service():
    customers = list(Customer.query.order_by(Customer.customer_name).all())
    if request.method == "POST":
        service = Service(
        service_type=request.form.get("service_type"),
        service_description=request.form.get("service_description"),
        safety_issue=bool(True if request.form.get("safety_issue") else False),
        next_service=request.form.get("next_service"),
        customer_id=request.form.get("customer_id")
        )
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_service.html", customers=customers)

@app.route("/edit_service/<int:service_id>", methods=["GET", "POST"])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    customers = list(Customer.query.order_by(Customer.customer_name).all())
    if request.method == "POST":
        service.service_type = request.form.get("service_type")
        service.service_description = request.form.get("service_description")
        service.safety_issue = bool(True if request.form.get("safety_issue") else False)
        service.next_service = request.form.get("next_service")
        service.customer_id = request.form.get("customer_id")
        db.session.commit()
    return render_template("edit_service.html", service=service, customers=customers)


@app.route("/delete_service/<int:service_id>")
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("home"))
