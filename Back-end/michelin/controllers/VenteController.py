from michelin.models.Vente import Vente
from michelin.models.Article import Article
from flask import jsonify, request
from extension import db


class VenteController:
    def __init__(self):
        self.vente_model = Vente
        self.article_model = Article

    def all(self):
        try:
            ventes = self.vente_model.query.all()
            result = [{'id': vente.id, 'prix': vente.prix, 'quantite': vente.quantite, 'article': vente.article.libelle,
                       'atelier': vente.atelier.nom, 'categorie': vente.categorie.libelle, 'date':vente.date, 'mois':vente.mois } for vente in ventes]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            date = request.form['date']
            prix = request.form['prix']
            quantite = int(request.form['quantite'])
            mois = request.form['mois']
            article_id = request.form['article_id']
            atelier_id = request.form['atelier_id']
            categorie_id = request.form['categorie_id']

            article = Article.query.get(article_id)
            article.quantite -= quantite
            vente = self.vente_model(date=date, prix=prix, quantite=quantite, mois=mois, article_id=article_id, categorie_id=categorie_id, atelier_id=atelier_id)
            db.session.add(vente)
            db.session.commit()

            return jsonify({'message': 'vente créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self, vente_id):
        try:
            vente = self.vente_model.query.get(vente_id)
            if not vente:
                return jsonify({'message': 'vente introuvable'}), 404

            article = Article.query.get(vente.article_id)
            article.quantite += vente.quantite

            db.session.delete(vente)
            db.session.commit()

            return jsonify({'message': 'vente supprimé avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

    def update(self, vente_id):
        try:
            vente = self.vente_model.query.get(vente_id)
            if not vente:
                return jsonify({'message': 'vente introuvable'}), 404

            ancienne_quantite = vente.quantite
            article = Article.query.get(vente.article_id)

            date = request.form.get('date', vente.date)
            prix = request.form.get('prix', vente.prix)
            quantite = int(request.form.get('quantite', vente.quantite))
            article_id = request.form.get('article_id', vente.article_id)
            mois = request.form.get('mois_id', vente.mois)
            atelier_id = request.form.get('atelier_id', vente.atelier_id)
            categorie_id = request.form.get('categorie_id', vente.categorie_id)

            vente.date = date
            vente.prix = prix
            vente.quantite = quantite
            vente.article_id = article_id
            vente.mois = mois
            vente.categorie_id = categorie_id
            vente.atelier_id = atelier_id

            article.quantite += ancienne_quantite - quantite

            db.session.commit()

            return jsonify({'message': 'Vente mis à jour avec succès'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
