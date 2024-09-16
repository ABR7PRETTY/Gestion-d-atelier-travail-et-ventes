from extension import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
    categorie = db.relationship('Categorie', backref=db.backref('articles', lazy=True))
    atelier_id = db.Column(db.Integer, db.ForeignKey('atelier.id'), nullable=False)
    atelier = db.relationship('Atelier', backref=db.backref('articles', lazy=True))



