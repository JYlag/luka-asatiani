from app import db
from hashutils import make_pw_hash

class Image(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(48))
    caption = db.Column(db.String(140))
    date = db.Column(db.Date)
    image_path = db.Column(db.String(140))

    def __init__(self, category, caption, date, image_path):
        self.category = category
        self.caption = caption
        self.date = date
        self.image_path = image_path

    def __repr__(self):
        return '<IMAGE &r' & self.image_path