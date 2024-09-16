from extension import db
import os
from werkzeug.utils import secure_filename

upload_folder = 'static'
os.makedirs(upload_folder, exist_ok=True)


class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    def save_image(self, image_file):
        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(upload_folder, filename)
            image_file.save(image_path)
            self.image = filename
            db.session.commit()
