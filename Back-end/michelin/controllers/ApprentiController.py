from michelin.models.Apprenti import Apprenti
from flask import jsonify, request
from extension import db


class ApprentiController:
    def __init__(self):
        self.apprenti_model = Apprenti

    def all(self):
        try:
            apprentis = self.apprenti_model.query.all()
            result = [{'id': apprenti.id, 'nom': apprenti.nom, 'prenom': apprenti.prenom, 'age': apprenti.age, 'grade': apprenti.grade, 'tuteur': apprenti.tuteur, 'atelier': apprenti.atelier.nom,
                       'image': apprenti.image} for apprenti in apprentis]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            nom = request.form['nom']
            prenom = request.form['prenom']
            age = request.form['age']
            grade = request.form['grade']
            tuteur = request.form['tuteur']
            atelier_id = request.form['atelier_id']

            if 'image' not in request.files:
                return jsonify({'message': 'Aucun fichier image'}), 400
            image = request.files['image']
            apprenti = self.apprenti_model(nom=nom, prenom=prenom,age=age, grade=grade, tuteur=tuteur,
                                           atelier_id=atelier_id)
            apprenti.save_image(image)
            db.session.add(apprenti)
            db.session.commit()

            return jsonify({'message': 'apprenti créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
    def delete(self, apprenti_id):
        try:
            apprenti = self.apprenti_model.query.get(apprenti_id)
            if not apprenti:
                return jsonify({'message': 'apprenti introuvable'}), 404

            db.session.delete(apprenti)
            db.session.commit()

            return jsonify({'message': 'apprenti supprimé avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500


    def update(self, apprenti_id):
        try:
            apprenti = self.apprenti_model.query.get(apprenti_id)
            if not apprenti:
                return jsonify({'message': 'apprenti introuvable'}), 404

            nom = request.form.get('nom', apprenti.nom)
            prenom = request.form.get('prenom', apprenti.prenom)
            age = request.form.get('age', apprenti.age)
            grade = request.form.get('grade', apprenti.grade)
            tuteur = request.form.get('tuteur', apprenti.tuteur)
            atelier_id = request.form.get('atelier_id', apprenti.atelier_id)

            if 'image' not in request.files:
                return jsonify({'message': 'Aucun fichier image'}), 400

            if 'image' in request.files:
                image = request.files['image']
                apprenti.save_image(image)

            apprenti.nom = nom
            apprenti.prenom = prenom
            apprenti.age = age
            apprenti.grade = grade
            apprenti.tuteur = tuteur
            apprenti.atelier_id = atelier_id
            db.session.commit()

            return jsonify({'message': 'apprenti mis à jour avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500
