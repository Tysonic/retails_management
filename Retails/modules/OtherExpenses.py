from Retails import db


class OtherExpenses(db.Model):
    Id = db.Column(db.Integer, primary_key=True, index=True)
    amount_spent = db.Column(db.Integer)
    date_spent = db.Column(db.DateTime)
    spend_on = db.Column(db.String)
    spend_by = db.Column(db.String)
    permitted_by = db.Column(db.String)
    details = db.Column(db.String)
    recorded_at = db.Column(db.String)

    def __init__(self, amount_spent, date_spent, spend_on, spend_by, details, recorded_at,permitted_by):
        self.amount_spent = amount_spent
        self.date_spent = date_spent
        self.spend_on = spend_on
        self.spend_by = spend_by
        self.permitted_by = permitted_by
        self.details = details
        self.recorded_at = recorded_at

    def __repr__(self):
        return f"{self.amount_spent,self.date_spent, self.spend_by,self.spend_on, self.details, self.recorded_at, self.permitted_by }"
