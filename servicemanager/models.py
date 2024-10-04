from servicemanager import db


class Customer(db.Model):
    # Customer model
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(30), unique=True, nullable=False)
    services = db.relationship("Service", backref="customer", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ string representation
        return self.customer_name


class Service(db.Model):
    # schema for the Service model
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), unique=True, nullable=False)
    service_description = db.Column(db.Text, nullable=False)
    safety_issue = db.Column(db.Boolean, default=False, nullable=False)
    next_service = db.Column(db.Date, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id", ondelete="CASCADE"), nullable=False)
    
    def __repr__(self):
        # __repr__ string representation
        return "#{0} - Service: {1} | Safety Issue: {2}".format(
            self.id, self.service_type, self.safety_issue
        )
