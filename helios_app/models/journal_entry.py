from helios_app.extensions import db

# This model class is just placeholder for now. More accurate model 
# definitions will be added later when requirements are more defined.
class JournalEntry(db.Model):
    user_id = db.Column(db.UUID, primary_key=True)
    post_date = db.Column(db.Timestamp)
    title = db.COlumn(db.String(100))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Journal Entry: "{self.title}">'