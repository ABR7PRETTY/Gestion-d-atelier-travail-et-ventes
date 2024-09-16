from extension import db


class Depense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    montant = db.Column(db.Integer, nullable=False)
    atelier_id = db.Column(db.Integer, db.ForeignKey('atelier.id'), nullable=False)
    atelier = db.relationship('Atelier', backref=db.backref('depenses', lazy=True))
    motif = db.Column(db.String(255), nullable=False)
    mois = db.Column(db.String(10), nullable=False)

