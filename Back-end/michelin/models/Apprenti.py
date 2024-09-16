from extension import db
import os
from werkzeug.utils import secure_filename

upload_folder = 'static'
os.makedirs(upload_folder, exist_ok=True)

class Apprenti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(25), unique=True, nullable=False)
    prenom = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    grade = db.Column(db.String(30), nullable=False)
    tuteur = db.Column(db.String(50), nullable=True)
    atelier_id = db.Column(db.Integer, db.ForeignKey('atelier.id'), nullable=False)
    atelier = db.relationship('Atelier', backref=db.backref('apprentis', lazy=True))

    def save_image(self, image_file):
        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(upload_folder, filename)
            image_file.save(image_path)
            self.image = filename
            db.session.commit()