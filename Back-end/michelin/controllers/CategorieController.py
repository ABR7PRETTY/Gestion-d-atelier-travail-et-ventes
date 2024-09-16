from michelin.models.Categorie import Categorie
from flask import jsonify, request
from extension import db


class CategorieController:
    def __init__(self):
        self.categorie_model = Categorie

    def all(self):
        try:
            categories = self.categorie_model.query.all()
            result = [{'id': categorie.id, 'libelle': categorie.libelle, 'description': categorie.description,
                       'image': categorie.image} for categorie in categories]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            libelle = request.form['libelle']
            description = request.form['description']

            if 'image' not in request.files:
                return jsonify({'message': 'Aucun fichier image'}), 400
            image = request.files['image']
            categorie = self.categorie_model(libelle=libelle,description=description)
            categorie.save_image(image)
            db.session.add(categorie)
            db.session.commit()

            return jsonify({'message': 'categorie créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
    def delete(self, categorie_id):
        try:
            categorie = self.categorie_model.query.get(categorie_id)
            if not categorie:
                return jsonify({'message': 'categorie introuvable'}), 404

            db.session.delete(categorie)
            db.session.commit()

            return jsonify({'message': 'categorie supprimé avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500


    def update(self, categorie_id):
        try:
            categorie = self.categorie_model.query.get(categorie_id)
            if not categorie:
                return jsonify({'message': 'categorie introuvable'}), 404

            libelle = request.form.get('libelle', categorie.libelle)
            description = request.form.get('description', categorie.description)

            if 'image' in request.files:
                image = request.files['image']
                categorie.save_image(image)

            categorie.libelle = libelle
            categorie.description = description
            db.session.commit()

            return jsonify({'message': 'categorie mis à jour avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500
