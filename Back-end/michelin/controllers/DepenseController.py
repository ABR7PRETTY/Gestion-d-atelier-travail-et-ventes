from michelin.models.Depense import Depense
from flask import jsonify, request
from extension import db


class DepenseController:
    def __init__(self):
        self.depense_model = Depense

    def all(self):
        try:
            depenses = self.depense_model.query.all()
            result = [{'id': depense.id, 'date': depense.date, 'montant': depense.montant, 'mois': depense.mois,
                       'motif': depense.motif, 'atelier': depense.atelier.nom
                       } for depense in depenses]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            date = request.form['date']
            montant = request.form['montant']
            motif = request.form['motif']
            mois = request.form['mois']
            atelier_id = request.form['atelier_id']

            depense = self.depense_model(date=date, montant=montant, mois=mois, motif=motif, atelier_id=atelier_id)
            db.session.add(depense)
            db.session.commit()

            return jsonify({'message': 'depense créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self, depense_id):
        try:
            depense = self.depense_model.query.get(depense_id)
            if not depense:
                return jsonify({'message': 'depense introuvable'}), 404

            db.session.delete(depense)
            db.session.commit()

            return jsonify({'message': 'depense supprimé avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

    def update(self, depense_id):
        try:
            depense = self.depense_model.query.get(depense_id)
            if not depense:
                return jsonify({'message': 'depense introuvable'}), 404

            date = request.form.get('date', depense.date)
            montant = request.form.get('montant', depense.montant)
            motif = request.form.get('motif', depense.motif)
            mois = request.form.get('mois', depense.mois)
            atelier_id = request.form.get('atelier_id', depense.atelier_id)

            depense.date = date
            depense.montant = montant
            depense.motif = motif
            depense.mois = mois
            depense.atelier_id = atelier_id
            db.session.commit()

            return jsonify({'message': 'depense mis à jour avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500
