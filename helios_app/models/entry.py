from helios_app.extensions import db

class Entry(db.Model):
    id = db.Column(db.UUID, primary_key=True)
    user_id = db.Column(db.UUID)
    content_url = db.Column(db.String(250))
    internal_view = db.Column(db.Integer)
    external_views = db.Column(db.Integer)
    journey_id = db.Colummn(db.UUID)
    create_timestamp = db.Column(db.TIMESTAMP)
    update_timestamp = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return f'<Entry "{self.id}">'