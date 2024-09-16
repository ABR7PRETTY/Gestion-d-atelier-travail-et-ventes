from michelin.models.Atelier import Atelier
from flask import jsonify, request
from extension import db


class AtelierController:
    def __init__(self):
        self.atelier_model = Atelier

    def all(self):
        try:
            ateliers = self.atelier_model.query.all()
            result = [{'id': atelier.id, 'nom': atelier.nom, 'localisation': atelier.localisation,
                       'image': atelier.image} for atelier in ateliers]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            nom = request.form['nom']
            localisation = request.form['localisation']

            if 'image' not in request.files:
                return jsonify({'message': 'Aucun fichier image'}), 400
            image = request.files['image']
            atelier = self.atelier_model(nom=nom, localisation=localisation)
            atelier.save_image(image)
            db.session.add(atelier)
            db.session.commit()

            return jsonify({'message': 'atelier créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
    def delete(self, atelier_id):
        try:
            atelier = self.atelier_model.query.get(atelier_id)
            if not atelier:
                return jsonify({'message': 'atelier introuvable'}), 404

            db.session.delete(atelier)
            db.session.commit()

            return jsonify({'message': 'atelier supprimé avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500


    def update(self, atelier_id):
        try:
            atelier = self.atelier_model.query.get(atelier_id)
            if not atelier:
                return jsonify({'message': 'atelier introuvable'}), 404

            nom = request.form.get('nom', atelier.nom)
            localisation = request.form.get('localisation', atelier.localisation)


            if 'image' in request.files:
                image = request.files['image']
                atelier.save_image(image)

            atelier.nom = nom
            atelier.localisation = localisation
            db.session.commit()

            return jsonify({'message': 'atelier mis à jour avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500
