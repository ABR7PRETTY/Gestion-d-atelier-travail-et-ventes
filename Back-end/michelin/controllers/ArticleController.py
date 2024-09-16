from michelin.models.Article import Article
from flask import jsonify, request
from extension import db


class ArticleController:
    def __init__(self):
        self.article_model = Article

    def all(self):
        try:
            articles = self.article_model.query.all()
            result = [{'id': article.id, 'libelle': article.libelle, 'prix': article.prix, 'quantite': article.quantite, 'categorie': article.categorie.libelle,
                       'atelier': article.atelier.nom, } for article in articles]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            libelle = request.form['libelle']
            prix = request.form['prix']
            quantite = request.form['quantite']
            categorie_id = request.form['categorie_id']
            atelier_id = request.form['atelier_id']
            article = self.article_model(libelle=libelle, prix=prix, quantite=quantite, categorie_id=categorie_id, atelier_id=atelier_id)
            db.session.add(article)
            db.session.commit()

            return jsonify({'message': 'article créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
    def delete(self, article_id):
        try:
            article = self.article_model.query.get(article_id)
            if not article:
                return jsonify({'message': 'article introuvable'}), 404

            db.session.delete(article)
            db.session.commit()

            return jsonify({'message': 'article supprimé avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500


    def update(self, article_id):
        try:
            article = self.article_model.query.get(article_id)
            if not article:
                return jsonify({'message': 'article introuvable'}), 404

            libelle = request.form.get('libelle', article.libelle)
            prix = request.form.get('prix', article.prix)
            quantite = request.form.get('quantite', article.quantite)
            categorie_id = request.form.get('categorie_id', article.categorie_id)
            atelier_id = request.form.get('atelier_id', article.atelier_id)

            article.libelle = libelle
            article.prix = prix
            article.quantite = quantite
            article.categorie_id = categorie_id
            article.atelier_id = atelier_id
            db.session.commit()

            return jsonify({'message': 'Article mis à jour avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500
