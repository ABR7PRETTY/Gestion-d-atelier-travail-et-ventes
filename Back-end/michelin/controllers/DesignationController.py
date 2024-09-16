from michelin.models.DesignationJournaliere import DesignationJournaliere
from flask import jsonify, request
from extension import db


class Designation_journaliereController:
    def __init__(self):
        self.designation_journaliere_model = DesignationJournaliere

    def all(self):
        try:
            designation_journalieres = self.designation_journaliere_model.query.all()
            result = [{'id': designation_journaliere.id, 'date': designation_journaliere.date, 'travail': designation_journaliere.travail, 'mois': designation_journaliere.mois, 'atelier': designation_journaliere.atelier.nom
                       } for designation_journaliere in designation_journalieres]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            date = request.form['date']
            travail = request.form['travail']
            mois = request.form['mois']
            atelier_id = request.form['atelier_id']

            designation_journaliere = self.designation_journaliere_model(date=date, travail=travail, mois=mois, atelier_id=atelier_id)
            db.session.add(designation_journaliere)
            db.session.commit()

            return jsonify({'message': 'designation journaliere créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
    def delete(self, designation_journaliere_id):
        try:
            designation_journaliere = self.designation_journaliere_model.query.get(designation_journaliere_id)
            if not designation_journaliere:
                return jsonify({'message': 'designation journaliere introuvable'}), 404

            db.session.delete(designation_journaliere)
            db.session.commit()

            return jsonify({'message': 'designation journaliere supprimé avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500


    def update(self, designation_journaliere_id):
        try:
            designation_journaliere = self.designation_journaliere_model.query.get(designation_journaliere_id)
            if not designation_journaliere:
                return jsonify({'message': 'designation introuvable'}), 404

            date = request.form.get('date', designation_journaliere.date)
            travail = request.form.get('travail', designation_journaliere.travail)
            mois = request.form.get('mois', designation_journaliere.mois)
            atelier_id = request.form.get('atelier_id', designation_journaliere.atelier_id)

            designation_journaliere.date = date
            designation_journaliere.travail = travail
            designation_journaliere.mois = mois
            designation_journaliere.atelier_id = atelier_id
            db.session.commit()

            return jsonify({'message': 'designation mis à jour avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500
