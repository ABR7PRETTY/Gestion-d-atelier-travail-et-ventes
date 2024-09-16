from extension import db



class Vente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    article = db.relationship('Article', backref=db.backref('ventes', lazy=True))
    atelier_id = db.Column(db.Integer, db.ForeignKey('atelier.id'), nullable=False)
    atelier = db.relationship('Atelier', backref=db.backref('ventes', lazy=True))
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
    categorie = db.relationship('Categorie', backref=db.backref('ventes', lazy=True))
    mois = db.Column(db.String(10), nullable=False)

