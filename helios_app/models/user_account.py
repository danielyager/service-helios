from helios_app.extensions import db

class UserAccount(db.Model):
    id = db.Column(db.UUID, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    email_confirmed = db.Column(db.Boolean)
    password = db.Column(db.String(25))
    phone_number = db.Column(db.String(10))
    phone_confirmed = db.Column(db.Boolean)
    create_timestamp = db.Column(db.TIMESTAMP)
    update_timestamp = db.Column(db.TIMESTAMP)
    last_login = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return f'<User Account "{self.email}">'