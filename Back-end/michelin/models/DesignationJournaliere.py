from extension import db


class DesignationJournaliere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    travail = db.Column(db.Integer, nullable=False)
    mois = db.Column(db.String(10), nullable=False)
    atelier_id = db.Column(db.Integer, db.ForeignKey('atelier.id'), nullable=False)
    atelier = db.relationship('Atelier', backref=db.backref('Designation_journalieres', lazy=True))
